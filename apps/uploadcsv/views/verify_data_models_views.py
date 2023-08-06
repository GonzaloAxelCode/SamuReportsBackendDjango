from rest_framework.permissions import AllowAny
from django.apps import apps
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import camel_case_to_spaces

class VerificarDatosAPIView(View):
    permission_classes = [AllowAny]
    
    def get(self, request):
        try:
            modelos = apps.get_app_config('uploadcsv').get_models()

            respuesta = []
            for modelo in modelos:
                objetos = modelo.objects.all()
                tiene_datos = objetos.exists()

                properties = []
                for field in modelo._meta.get_fields():
                    if field.concrete:
                        properties.append({ 'namePropertie': field.name })

                nombre_modelo = modelo.__name__   
                title = nombre_modelo.replace("_", " ").title()

                respuesta.append({
                    'nombre_modelo': modelo.__name__,
                    'tiene_datos': not tiene_datos,
                    'properties': properties,
                    'title': title

                })

            return JsonResponse(respuesta, safe=False)

        except ObjectDoesNotExist:
            respuesta = {
                'error': 'No se encontraron modelos en la aplicación.',
            }
            return JsonResponse(respuesta, status=404)
