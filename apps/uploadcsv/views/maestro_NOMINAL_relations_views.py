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
import csv
import io
from django.http import HttpResponse


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


class MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_CSV_Export_View(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Query the database to get all records from your model
        queryset = MAESTRO_HIS_NUEVO_ARCHIVO_PLANO.objects.all()

        # Define the CSV file response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Create a CSV writer and write the header row
        writer = csv.writer(response)
        header = [
            "Id", "Id_Cita", "Anio", "Mes", "Dia", "Fecha_Atencion",
            "Lote", "Num_Pag", "Num_Reg", "Id_Ups", "Id_Establecimiento",
            "Id_Paciente", "Id_Personal", "Id_Registrador", "Id_Financiador",
            "Id_Condicion_Establecimiento", "Id_Condicion_Servicio", "Edad_Reg",
            "Tipo_Edad", "Anio_Actual_Paciente", "Mes_Actual_Paciente",
            "Dia_Actual_Paciente", "Id_Turno", "Codigo_Item", "Tipo_Diagnostico",
            "Peso", "Talla", "Hemoglobina", "Perimetro_Abdominal",
            "Perimetro_Cefalico", "Id_Otra_Condicion", "Id_Centro_Poblado",
            "Id_Correlativo", "Id_Correlativo_Lab", "Valor_Lab",
            "Fecha_Ultima_Regla", "Fecha_Solicitud_Hb", "Fecha_Resultado_Hb",
            "Fecha_Registro", "Fecha_Modificacion", "Id_Pais"
        ]

        writer.writerow(header)

        # Write the data rows
        for record in queryset:
            # Replace None with empty string in each field
            row = [
                str(record.Id or ''),
                record.Id_Cita or '',
                str(record.Anio or ''),
                str(record.Mes or ''),
                str(record.Dia or ''),
                record.Fecha_Atencion or '',
                record.Lote or '',
                str(record.Num_Pag or ''),
                str(record.Num_Reg or ''),
                str(record.Id_Ups_id or ''),
                str(record.Id_Establecimiento_id or ''),
                str(record.Id_Paciente_id or ''),
                str(record.Id_Personal_id or ''),
                str(record.Id_Registrador_id or ''),
                str(record.Id_Financiador_id or ''),
                record.Id_Condicion_Establecimiento or '',
                record.Id_Condicion_Servicio or '',
                str(record.Edad_Reg or ''),
                record.Tipo_Edad or '',
                str(record.Anio_Actual_Paciente or ''),
                str(record.Mes_Actual_Paciente or ''),
                str(record.Dia_Actual_Paciente or ''),
                record.Id_Turno or '',
                str(record.Codigo_Item_id or ''),
                record.Tipo_Diagnostico or '',
                str(record.Peso or ''),
                str(record.Talla or ''),
                str(record.Hemoglobina or ''),
                str(record.Perimetro_Abdominal or ''),
                str(record.Perimetro_Cefalico or ''),
                str(record.Id_Otra_Condicion_id or ''),
                str(record.Id_Centro_Poblado_id or ''),
                str(record.Id_Correlativo or ''),
                str(record.Id_Correlativo_Lab or ''),
                record.Valor_Lab or '',
                record.Fecha_Ultima_Regla or '',
                record.Fecha_Solicitud_Hb or '',
                record.Fecha_Resultado_Hb or '',
                record.Fecha_Registro or '',
                record.Fecha_Modificacion or '',
                str(record.Id_Pais_id or '')
            ]

            writer.writerow(row)

        return response
