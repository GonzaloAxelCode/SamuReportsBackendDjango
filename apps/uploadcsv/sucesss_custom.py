from enum import Enum
from rest_framework.response import Response
from rest_framework import status

class SuccessType(Enum):
    DATA_PROCESSED = 'Data processed successfully'

class ResultType(dict):
    def __init__(self,
            message=None,
            success_type=SuccessType.DATA_PROCESSED,    
            total_data_csv_original=None,
            total_data_csv_partida=None,
            total_despues_procesamiento=None,
            total_objetos_creados=None,
            total_datos_guardados_database=None,
            time=None,
        ):
                    super().__init__()
                    self['message'] = message
                    self['success_type'] = success_type.value
                    self['total_data_csv_original'] = total_data_csv_original
                    self['total_data_csv_partida'] = total_data_csv_partida
                    self['total_despues_procesamiento'] = total_despues_procesamiento
                    self['total_objetos_creados'] = total_objetos_creados
                    self['total_datos_guardados_database'] = total_datos_guardados_database
                    self['time'] = time

                


