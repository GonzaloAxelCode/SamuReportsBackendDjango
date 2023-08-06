from venv import logger
from django.db import connection
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from apps.uploadcsv.custom_errors import CustomError
from apps.uploadcsv.utils import CustomPageNumberPagination
from apps.uploadcsv.sucesss_custom import ResultType, SuccessType
from apps.uploadcsv.testOperation import DataExcelCNVValidator, ObjectOperations, ServiceDatabase
from apps.uploadcsv.serializers import DATA_CNVSerializer
from apps.uploadcsv.models import DATA_CNV
import time


class DATA_CNV_CSV_View(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        start_time = time.time()
        model = DATA_CNV
        instance = DATA_CNV()
        identifier_field = "CNV"
        try:
            # leer
            csv_file = request.FILES.get('csv_file')
            dataframe = DataExcelCNVValidator(csv_file)
            columns_to_convert = [
                'Edad', 'Gest(Sem)', 'Peso(g)', 'Talla(cm)', 'Apgar', 'Perímetro cefálico', 'Perímetro torácico', 'Unnamed: 33', 'Unnamed: 35'
            ]
            columns_to_ignore = [
                "Cod. EESS", "Cod. EESS Prenatal", "N° Colegio", "Teléfono", "CNV"]
            rename_columns = {
                "PrimerApellido": "pApellidoMadre",
                "Segundo": "sApellidoMadre",
                "Nombres": "nombresMadre",
                "PrimerApellido1": "pApellidoProfesional",
                "Segundo1": "sApellidoProfesional",
                "Nombres1": "nombresProfesional",
                "PrimerApellido2": "pApellidoResgistrador",
                "SegundoApellido": "sApellidoRegistrador",
                "Nombres2": "nombresRegistrador"
            }
            # procesar y verificar
            dataframe.validate_file_type()
            dataframe.read_excel_file(
                columns_to_convert=columns_to_convert, columns_to_str=columns_to_ignore)
            # Dividir la data en dos clases
            dataframe.divide_type_birth()
            dataframe.clean_data(columns_to_ignore=columns_to_ignore)
            dataframe.remove_special_characters_from_columns(
                rename_columns=rename_columns)
            dataframe.replace_none_strange_values()
            # operaciones y validaciones1
            objectDatrame = ObjectOperations(dataframe.data)
            objectDatrame.get_field_names_from_instance(instance)
            objectDatrame.validate_columns(objectDatrame.field_names)
            # Creacion de objetos con abase de datos
            database = ServiceDatabase(
                objectDatrame.data, identifier_field, model)
            database.create_objects_from_data()
            database.saveData()
            is_data_added = (database.data_count_save -
                             database.count_data_before) > 0
            end_time = time.time()
            elapsed_time = end_time - start_time
            result = ResultType(
                message=f'{database.data_count_save - database.count_data_before} registros agregados con éxito.' if is_data_added else 'Los registros existen en la base de datos.',
                success_type=SuccessType.DATA_PROCESSED,
                total_data_csv_original=dataframe.count_data_orignal_csv,
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


class DATA_CNV_Delete_View(APIView):
    permission_classes = [AllowAny]

    def delete(self, request):
        with connection.cursor() as cursor:
            table_name = DATA_CNV._meta.db_table
            cursor.execute(
                f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE;')
        return Response({'message': 'Todos los registros han sido eliminados.'}, status=status.HTTP_204_NO_CONTENT)


class DATA_CNV_List_View(generics.ListAPIView):
    queryset = DATA_CNV.objects.all()
    serializer_class = DATA_CNVSerializer
    pagination_class = CustomPageNumberPagination
