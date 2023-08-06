import time
from venv import logger

from apps.uploadcsv.custom_errors import CustomError
from apps.uploadcsv.mixins import FileValidationMixin
from apps.uploadcsv.models import MAESTRO_HIS_COLEGIO, MAESTRO_HIS_CONDICION_CONTRATO, MAESTRO_HIS_ESTABLECIMIENTO, \
    MAESTRO_HIS_PERSONAL, MAESTRO_HIS_PROFESION, MAESTRO_HIS_TIPO_DOC
from apps.uploadcsv.serializers import MaestroPersonalSerializer
from apps.uploadcsv.sucesss_custom import ResultType, SuccessType
from apps.uploadcsv.testOperationsv2 import DataframeOperations, ObjectsOperations

from apps.uploadcsv.utils import CustomPageNumberPagination
from django.db import connection
from django.forms import ValidationError
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

import numpy as np


class MAESTRO_HIS_PERSONAL_CSV_View_test(APIView, FileValidationMixin):
    permission_classes = [AllowAny]

    def post(self, request):
        start_time = time.time()

        model = MAESTRO_HIS_PERSONAL
        identifier_field = "Id_Personal"
        dtypes = {
            "Id_Personal": np.int64,
            "Numero_Documento": str,
            "Apellido_Paterno_Personal": str,
            "Apellido_Materno_Personal": str,
            "Nombres_Personal": str,
            "Fecha_Nacimiento": str,
            "Numero_Colegiatura": str,
            "Fecha_Alta": str,
            "Fecha_Baja": str
        }
        foreign_keys = {
            'Id_Tipo_Documento': MAESTRO_HIS_TIPO_DOC,
            'Id_Condicion': MAESTRO_HIS_CONDICION_CONTRATO,
            'Id_Profesion': MAESTRO_HIS_PROFESION,
            'Id_Colegio': MAESTRO_HIS_COLEGIO,
            'Id_Establecimiento': MAESTRO_HIS_ESTABLECIMIENTO,
        }

        try:
            # leer
            csv_file = request.FILES.get('csv_file')

            dataframe = DataframeOperations(csv_file, identifier_field)
            dataframe.read_csv_file(dtypes=dtypes)
            dataframe.validate_file_type()
            dataframe.clean_data()
            dataframe.prepare_dataframe()

            objects = ObjectsOperations(
                dataframe.data, identifier_field, model)
            objects.validate_columns()

            objects.create_objects_with_relations(foreign_keys=foreign_keys)
            objects.save_objects_database()

            is_data_added = (objects.data_count_save -
                             objects.count_data_before) > 0

            end_time = time.time()
            elapsed_time = end_time - start_time

            result = ResultType(
                message=f'{objects.data_count_save - objects.count_data_before} registros agregados con éxito.' if is_data_added else 'Los registros existen en la base de datos.',
                success_type=SuccessType.DATA_PROCESSED,
                total_data_csv_original=dataframe.count_data_orignal_csv,
                total_despues_procesamiento=dataframe.count_data_processing,
                total_objetos_creados=objects.added_objects_count,
                total_datos_guardados_database=objects.data_count_save,
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


class MAESTRO_HIS_PERSONAL_Delete_View(APIView):
    permission_classes = [AllowAny]

    def delete(self, request):
        with connection.cursor() as cursor:
            # Trunca la tabla para eliminar todos los registros y reiniciar los contadores de secuencia
            table_name = MAESTRO_HIS_PERSONAL._meta.db_table
            cursor.execute(
                f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE;')

        return Response({'message': 'Todos los registros han sido eliminados.'}, status=status.HTTP_204_NO_CONTENT)


class MAESTRO_HIS_PERSONAL_List_View(generics.ListAPIView):

    queryset = MAESTRO_HIS_PERSONAL.objects.all()
    serializer_class = MaestroPersonalSerializer
    pagination_class = CustomPageNumberPagination
