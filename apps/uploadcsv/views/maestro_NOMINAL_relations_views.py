import csv
import time
from venv import logger

import numpy as np
from apps.uploadcsv.custom_errors import CustomError
from apps.uploadcsv.mixins import FileValidationMixin
from apps.uploadcsv.models import MAESTRO_HIS_CENTRO_POBLADO, MAESTRO_HIS_CIE_CPMS, MAESTRO_HIS_ESTABLECIMIENTO, \
    MAESTRO_HIS_FINANCIADOR, MAESTRO_HIS_NUEVO_ARCHIVO_PLANO, MAESTRO_HIS_OTRA_CONDICION, MAESTRO_HIS_PACIENTE, \
    MAESTRO_HIS_PAIS, MAESTRO_HIS_PERSONAL, MAESTRO_HIS_REGISTRADOR, MAESTRO_HIS_UPS
from apps.uploadcsv.serializers import MAESTRO_HIS_NUEVO_ARCHIVO_PLANOSerializer
from apps.uploadcsv.sucesss_custom import ResultType, SuccessType
from apps.uploadcsv.testOperation import DataValidator, ObjectOperations, ServiceDatabase
from apps.uploadcsv.utils import CustomPageNumberPagination
from django.db import connection
from django.forms import ValidationError
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_CSV_View_TEST(APIView, FileValidationMixin):
    permission_classes = [AllowAny]

    def post(self, request):
        start_time = time.time()

        model = MAESTRO_HIS_NUEVO_ARCHIVO_PLANO
        instance = model()
        identifier_field = "Id_Cita"

        try:
            # leer
            csv_file = request.FILES.get('csv_file')
            delimiter = request.data.get('delimiter')
            encode = request.data.get('encode')
            dataframe = DataValidator(csv_file)

            # procesar y verificar
            dataframe.validate_file_type()
            # dataframe.read_csv_file(use_cols=range(43),drop_cols=['condicion_gestante', 'peso_pregestacional', 'gruporiesgo_desc'])
            dataframe.read_csv_file(delimiter=delimiter, encoding=encode)
            dataframe.indexar()  # creamos un id Unico
            # dataframe.split_data(3000)

            dataframe.clean_data(columns_to_string=["Codigo_Item"])

            dataframe.replace_none_strange_values(values_=[])

            # operaciones y validaciones1
            objectDatrame = ObjectOperations(dataframe.data)
            objectDatrame.get_field_names_from_instance(instance)
            objectDatrame.validate_columns(
                objectDatrame.field_names)

            print(objectDatrame.data)

            # Creacion de objetos con abase de datos
            database = ServiceDatabase(
                objectDatrame.data, identifier_field, model)

            related_models = {
                'Id_Ups': MAESTRO_HIS_UPS,
                'Id_Establecimiento': MAESTRO_HIS_ESTABLECIMIENTO,
                'Id_Registrador': MAESTRO_HIS_REGISTRADOR,
                'Id_Financiador': MAESTRO_HIS_FINANCIADOR,
                'Codigo_Item': MAESTRO_HIS_CIE_CPMS,
                'Id_Otra_Condicion': MAESTRO_HIS_OTRA_CONDICION,
                'Id_Centro_Poblado': MAESTRO_HIS_CENTRO_POBLADO,
                'Id_Pais': MAESTRO_HIS_PAIS,
                'Id_Paciente': MAESTRO_HIS_PACIENTE,
                'Id_Personal': MAESTRO_HIS_PERSONAL,
            }

            database.create_objects_from_data_nominal(related_models)

            database.saveData(ignore_conflicts=True)
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


class MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_Delete_View_TEST(APIView):
    permission_classes = [AllowAny]

    def delete(self, request):
        with connection.cursor() as cursor:

            table_name = MAESTRO_HIS_NUEVO_ARCHIVO_PLANO._meta.db_table
            cursor.execute(
                f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE;')

        return Response({'message': 'Todos los registros han sido eliminados.'}, status=status.HTTP_204_NO_CONTENT)


class MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_List_View_TEST(generics.ListAPIView):

    queryset = MAESTRO_HIS_NUEVO_ARCHIVO_PLANO.objects.all()
    serializer_class = MAESTRO_HIS_NUEVO_ARCHIVO_PLANOSerializer
    pagination_class = CustomPageNumberPagination
