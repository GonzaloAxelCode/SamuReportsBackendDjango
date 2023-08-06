
''''


    VERSION DE FUNCIONALIDADES v.0.2
    
    Aun no en uso



'''
import numpy as np
import pandas as pd
from apps.uploadcsv.custom_errors import CustomError, ErrorType
from django.db import models
from django.db import transaction


class DataframeOperations:
    def __init__(self, File, identifier_field):
        self.data = None
        self.file = File
        self.identifier_field = identifier_field
        self.count_data_orignal_csv = 0
        self.count_data_processing = 0

    def validate_file_type(self):
        if not self.file.name.lower().endswith('.csv'):
            raise CustomError(
                error_type=ErrorType.FILE_TYPE_ERROR,
                message='El archivo debe ser de tipo CSV.'
            )

    def read_csv_file(self, delimiter=";", encoding='utf-8', dtypes={}):
        self.data = pd.read_csv(self.file, dtype=dtypes)
        self.count_data_orignal_csv = len(self.data)

    def clean_data(self):
        self.data.drop_duplicates(
            subset=[self.identifier_field], keep='first', inplace=True)

        # Reemplazar valores faltantes (NaN) con None
        self.data = self.data.where(pd.notnull(self.data), None)

        self.count_data_processing = len(self.data)

    def prepare_dataframe(self):

        trash_values = ["", "None", "NaT", "N/A", "<NA>.", "n/a", "null",
                        "nan" "NULL", "-", "<NA>", "<nan>", "#N/A", "#N/A N/A", 'SIN DA',
                        'nullnu', "Id_Cita", "'None'", "Anio", "Mes", "Dia", "Fecha_Atencion",
                        "Lote", "Num_Pag",    "Num_Reg",    "Id_Ups",    "Id_Establecimiento",
                        "Id_Paciente", "Id_Personal",    "Id_Registrador",    "Id_Financiador",
                        "Id_Condicion_Establecimiento",    "Id_Condicion_Servicio",    "Edad_Reg",
                        "Tipo_Edad",    "Anio_Actual_Paciente",    "Mes_Actual_Paciente",
                        "Dia_Actual_Paciente",    "Id_Turno",    "Codigo_Item",    "Tipo_Diagnostico",
                        "Valor_Lab",    "Id_Correlativo",    "Id_Correlativo_Lab",    "Peso",    "Talla",
                        "Hemoglobina",    "Perimetro_Abdominal",    "Perimetro_Cefalico",    "Id_Otra_Condicion",
                        "Id_Centro_Poblado",    "Fecha_Ultima_Regla",    "Fecha_Solicitud_Hb",
                        "Fecha_Resultado_Hb", "Fecha_Registro", "Fecha_Modificacion", "Id_Pais"]

        replace_dict = {s: None for s in trash_values}
        self.data = self.data.replace(replace_dict)


class ObjectsOperations:

    def __init__(self, data, identifier_field, model):
        self.data = data
        self.field_names = []
        self.objects = []
        self.model = model
        self.identifier_field = identifier_field
        self.added_objects_count = 0
        self.data_count_save = 0
        self.count_data_before = self.model.objects.all().count()

    def validate_columns(self, excluded_columns=[]):
        fields = self.model()._meta.fields
        expected_columns = [field.name for field in fields]

        expected_columns = [
            field for field in expected_columns if field not in excluded_columns]

        missing_columns = [
            column for column in expected_columns if column not in self.data.columns]

        new_columns = [
            column for column in self.data.columns if column not in expected_columns]

        error_messages = []

        if missing_columns or new_columns:
            if missing_columns:

                error_messages.append(
                    f'Faltan Columnas.')

            if new_columns:
                if not missing_columns:
                    error_messages.append(
                        f'Todas las columnas estan incluidas ya.')
                error_messages.append(
                    f' Hay columnas que son nuevas o estan mal escritas.')
                error_messages.append(
                    f'Intente verificar su archivo .CSV que tengan las mismas columnas')

            raise CustomError(
                error_type=ErrorType.VALIDATION_ERROR,
                message=' '.join(error_messages),
                expected_columns=expected_columns,
                details={
                    'missing_columns': missing_columns,
                    'new_columns': new_columns,
                }
            )

    def create_objects(self):
        try:
            existing_ids = self.model.objects.values_list(
                self.identifier_field, flat=True)
            self.data = self.data[~self.data[self.identifier_field].isin(
                existing_ids)]

            unique_objects = {}
            for _, row in self.data.iterrows():
                row_dict = row.to_dict()
                id_value = row_dict[self.identifier_field]
                if id_value not in unique_objects:
                    unique_objects[id_value] = self.model(**row_dict)

            self.objects = list(unique_objects.values())
            self.added_objects_count = len(self.objects)

        except Exception as e:
            raise CustomError(
                error_type=ErrorType.DATABASE_ERROR,
                message=f'Ocurrió un error al crear objetos de tipo {self.model.__name__}.',
                details={'error_details': str(e)}
            )

    def create_objects_with_relations(self, foreign_keys=None):

        if foreign_keys is None:
            foreign_keys = {}

        fk_cache = {fk_field: {} for fk_field in foreign_keys.keys()}

        def get_fk_object(fk_field, fk_value):
            if fk_value is None:
                return None
            elif fk_value in fk_cache[fk_field]:
                return fk_cache[fk_field][fk_value]
            else:
                fk_model = foreign_keys[fk_field]

            try:
                fk_object, _ = fk_model.objects.get_or_create(pk=fk_value)
            except Exception as e:
                return None

            fk_cache[fk_field][fk_value] = fk_object
            return fk_object

        try:
            for fk_field in foreign_keys.keys():
                self.data[fk_field] = self.data[fk_field].apply(
                    lambda fk_value: get_fk_object(fk_field, fk_value))

        except Exception as e:

            raise CustomError(
                error_type=ErrorType.DATABASE_ERROR,
                message=f'Ocurrió un error al filtrar llaves foraneas',
                details={'error_details': str(e)}
            )
        try:
            self.objects = [self.model(**row._asdict())
                            for row in self.data.itertuples(index=False)]

            self.added_objects_count = len(self.objects)

        except Exception as e:
            raise CustomError(
                error_type=ErrorType.DATABASE_ERROR,
                message=f'Ocurrió un error al crear objetos de tipo {self.model.__name__}.',
                details={'error_details': str(e)}
            )

    def save_objects_database(self, ignore_conflicts=False, batch_size=2000):
        with transaction.atomic():
            for i in range(0, len(self.objects), batch_size):
                batch_data = self.objects[i:i+batch_size]
                self.model.objects.bulk_create(
                    batch_data, ignore_conflicts=ignore_conflicts)
                print(len(batch_data))

        self.data_count_save = self.model.objects.all().count()
