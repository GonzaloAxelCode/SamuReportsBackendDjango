from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F

from apps.uploadcsv.models import DATA_CNV, MAESTRO_HIS_PACIENTE


class CNV_RELATION_PACIENTEView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            registros_cnv = DATA_CNV.objects.all()

            # Iterar sobre los registros de DATA_CNV
            for registro_cnv in registros_cnv:
                # Buscar los registros de MAESTRO_HIS_PACIENTE donde Numero_Documento sea igual a CNV
                pacientes = MAESTRO_HIS_PACIENTE.objects.filter(
                    Numero_Documento=registro_cnv.CNV)

                # Actualizar el campo CNV_id de cada paciente con el valor de CNV de DATA_CNV
                pacientes.update(CNV_id=registro_cnv.CNV)

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': str(e)})
