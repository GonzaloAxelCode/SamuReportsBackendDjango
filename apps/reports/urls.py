from django.urls import path
from .views import MyView, MyView2

urlpatterns = [
    path('sp_condicion_pacientes', MyView.as_view(),
         name='sp_condicion_pacientes'),
    path('sp_indicador_fallo_hospital_ilo', MyView2.as_view(),
         name='sp_indicador_fallo_hospital_ilo'),

]
