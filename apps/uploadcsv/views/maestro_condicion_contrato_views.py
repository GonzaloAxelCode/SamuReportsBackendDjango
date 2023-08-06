import time
from venv import logger

from apps.uploadcsv.custom_errors import CustomError
from apps.uploadcsv.mixins import FileValidationMixin
from apps.uploadcsv.models import MAESTRO_HIS_CONDICION_CONTRATO
from apps.uploadcsv.serializers import MAESTRO_HIS_CONDICION_CONTRATOSerializer
from apps.uploadcsv.sucesss_custom import ResultType, SuccessType
from apps.uploadcsv.testOperation import DataValidator, ObjectOperations, ServiceDatabase
from apps.uploadcsv.utils import CustomPageNumberPagination
from django.db import connection
from django.forms import ValidationError
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class MAESTRO_HIS_CONDICION_CONTRATO_CSV_View(APIView, FileValidationMixin):
    permission_classes = [AllowAny]

    def post(self, request):

        
        start_time = time.time()
        model = MAESTRO_HIS_CONDICION_CONTRATO
        instance = MAESTRO_HIS_CONDICION_CONTRATO()
        identifier_field = "Id_Condicion"
        try:
           #leer
            csv_file = request.FILES.get('csv_file')
            dataframe = DataValidator(csv_file)
            delimiter = request.data.get('delimiter')
            encode = request.data.get('encode')

            # procesar y verificar
            dataframe.validate_file_type()
            dataframe.read_csv_file(delimiter=delimiter,encoding=encode)    
            dataframe.clean_data()
            dataframe.replace_none_strange_values()
            
            #operaciones y validaciones1
            objectDatrame = ObjectOperations(dataframe.data)    
            objectDatrame.get_field_names_from_instance(instance)
            objectDatrame.validate_columns(objectDatrame.field_names)
            
            
            # Creacion de objetos con abase de datos 
            database = ServiceDatabase(objectDatrame.data,identifier_field,model)
           
            database.create_objects_from_data()
            database.saveData(ignore_conflicts=True)
            is_data_added =  (database.data_count_save - database.count_data_before ) > 0            
            
            end_time = time.time()  
            elapsed_time = end_time - start_time

            
            result = ResultType(
                message=f'{database.data_count_save - database.count_data_before} registros agregados con éxito.' if is_data_added else 'Los registros existen en la base de datos.',
                success_type=SuccessType.DATA_PROCESSED,
                total_data_csv_original= dataframe.count_data_orignal_csv,
                total_despues_procesamiento=dataframe.count_data_processing,
                total_objetos_creados=database.added_objects_count,
                total_datos_guardados_database=database.data_count_save,
                time=elapsed_time,
             )
                           
            return Response(result, status=status.HTTP_201_CREATED)


        except CustomError as e:
            end_time = time.time() 
            elapsed_time = end_time - start_time
            return Response(
                {

                    'error_type': e.error_type.value,
                    'message': e.message,
                    'details': e.details,
                    'expected_columns': e.expected_columns,
                    'time': elapsed_time,  

                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as e:
            return Response({
                'error_type': 'Error de validación',
                'message': f"Se encontró un problema con los datos proporcionados: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as e:
            return Response({
                'error_type': 'Error de clave',
                'message': f"Se intentó acceder a una clave que no existe: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({
                'error_type': 'Error de valor',
                'message': f"Se encontró un problema con el valor proporcionado: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            return Response({
                'error_type': 'Error de tipo',
                'message': f"Se encontró un problema con el tipo de objeto utilizado: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("Ocurrió un error no manejado específicamente")  
            return Response({
                'error_type': 'Error genérico',
                'message': f"Ocurrió un error no especificado: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)


class MAESTRO_HIS_CONDICION_CONTRATO_Delete_View(APIView):
   permission_classes = [AllowAny]
   def delete(self, request):
        with connection.cursor() as cursor:
            # Trunca la tabla para eliminar todos los registros y reiniciar los contadores de secuencia
            table_name =  MAESTRO_HIS_CONDICION_CONTRATO._meta.db_table
            cursor.execute(
                f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE;')

        return Response({'message': 'Todos los registros han sido eliminados.'}, status=status.HTTP_204_NO_CONTENT)



class MAESTRO_HIS_CONDICION_CONTRATO_List_View(generics.ListAPIView):
   


    queryset = MAESTRO_HIS_CONDICION_CONTRATO.objects.all()
    serializer_class = MAESTRO_HIS_CONDICION_CONTRATOSerializer
    pagination_class = CustomPageNumberPagination

