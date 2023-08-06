from enum import Enum


class ErrorType(Enum):
    INVALID_PRIMARY_KEY = 'El_identificador_principal_es_inválido'
    ENCODING_ERROR = 'Error_de_codificación'
    VALIDATION_ERROR = 'Error_de_validación_de_columna'
    DATABASE_ERROR = 'Error_de_base_de_datos'
    FILE_FORMAT_ERROR = 'Error_de_formato_de_archivo'
    FILE_TYPE_ERROR = 'Error_de_tipo_de_archivo'
    DATAFRAME_DTYPE_CONVERSION_ERROR = 'Error_de_conversión_de_tipo_de_datos_en_el_dataframe'
    VALIDATE_ERROR = 'Error_de_validación'
    KEY_ERROR = 'Error_de_clave'
    ERROR_VALUE = 'Error_de_valor_de_clave'
    ERROR_TYPE = 'Error_de_tipo'
    UNKNOWN_ERROR = 'Error_desconocido'



class CustomError(Exception):
    def __init__(self, error_type: ErrorType, message,  expected_columns=[],details=None):
        super().__init__(message)
        self.error_type = error_type
        self.message = message
        self.details = details
        self.expected_columns = expected_columns
