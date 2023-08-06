from apps.uploadcsv.views.cnv_relation_to_paciente import CNV_RELATION_PACIENTEView
from apps.uploadcsv.views.maestro_actividad_views import MAESTRO_HIS_ACTIVIDAD_HIS_CSV_View, \
    MAESTRO_HIS_ACTIVIDAD_HIS_Delete_View, MAESTRO_HIS_ACTIVIDAD_HIS_List_View
from apps.uploadcsv.views.maestro_centropoblado_views import MAESTRO_HIS_CENTRO_POBLADO_CSV_View, \
    MAESTRO_HIS_CENTRO_POBLADO_Delete_View, MAESTRO_HIS_CENTRO_POBLADO_List_View
from apps.uploadcsv.views.maestro_colegio_views import MAESTRO_HIS_COLEGIO_CSV_View, MAESTRO_HIS_COLEGIO_Delete_View, \
    MAESTRO_HIS_COLEGIO_List_View
from apps.uploadcsv.views.maestro_condicion_contrato_views import MAESTRO_HIS_CONDICION_CONTRATO_CSV_View, \
    MAESTRO_HIS_CONDICION_CONTRATO_Delete_View, MAESTRO_HIS_CONDICION_CONTRATO_List_View
from apps.uploadcsv.views.maestro_cpms_views import MAESTRO_HIS_CIE_CPMS_CSV_View, MAESTRO_HIS_CIE_CPMS_Delete_View, \
    MAESTRO_HIS_CIE_CPMS_List_View
from apps.uploadcsv.views.maestro_establecimiento_views import MAESTRO_HIS_ESTABLECIMIENTO_CSV_View, \
    MAESTRO_HIS_ESTABLECIMIENTO_Delete_View, MAESTRO_HIS_ESTABLECIMIENTO_List_View
from apps.uploadcsv.views.maestro_etnia_views import MAESTRO_HIS_ETNIA_CSV_View, MAESTRO_HIS_ETNIA_Delete_View, \
    MAESTRO_HIS_ETNIA_List_View
from apps.uploadcsv.views.maestro_financiador import MAESTRO_HIS_FINANCIADOR_CSV_View, \
    MAESTRO_HIS_FINANCIADOR_Delete_View, MAESTRO_HIS_FINANCIADOR_List_View
from apps.uploadcsv.views.maestro_NOMINAL_relations_views import MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_CSV_View_TEST, \
    MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_Delete_View_TEST, MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_List_View_TEST
from apps.uploadcsv.views.maestro_otra_condicion_views import MAESTRO_HIS_OTRA_CONDICION_CSV_View, \
    MAESTRO_HIS_OTRA_CONDICION_Delete_View, MAESTRO_HIS_OTRA_CONDICION_List_View
from apps.uploadcsv.views.maestro_paciente_relation import MAESTRO_HIS_PACIENTE_CSV_View, \
    MAESTRO_HIS_PACIENTE_Delete_View, MAESTRO_HIS_PACIENTE_List_View
from apps.uploadcsv.views.maestro_pais_views import MAESTRO_HIS_PAIS_CSV_View, MAESTRO_HIS_PAIS_Delete_View, \
    MAESTRO_HIS_PAIS_List_View
from apps.uploadcsv.views.maestro_personal_relation_views import MAESTRO_HIS_PERSONAL_CSV_View, \
    MAESTRO_HIS_PERSONAL_Delete_View, MAESTRO_HIS_PERSONAL_List_View
from apps.uploadcsv.views.maestro_personal_relation_views_____copy import MAESTRO_HIS_PERSONAL_CSV_View_test
from apps.uploadcsv.views.maestro_profesion_relation_views import MAESTRO_HIS_PROFESION_CSV_View, \
    MAESTRO_HIS_PROFESION_Delete_View, MAESTRO_HIS_PROFESION_List_View
from apps.uploadcsv.views.maestro_registrador_relation_views import MAESTRO_HIS_REGISTRADOR_CSV_View, \
    MAESTRO_HIS_REGISTRADOR_Delete_View, MAESTRO_HIS_REGISTRADOR_List_View
from apps.uploadcsv.views.maestro_tipodoc_views import MAESTRO_HIS_TIPO_DOC_CSV_View, \
    MAESTRO_HIS_TIPO_DOC_Delete_View, MAESTRO_HIS_TIPO_DOC_List_View
from apps.uploadcsv.views.maestro_ubigeo_views import MAESTRO_HIS_UBIGEO_INEI_RENIEC_CSV_View, \
    MAESTRO_HIS_UBIGEO_INEI_RENIEC_Delete_View, MAESTRO_HIS_UBIGEO_INEI_RENIEC_List_View
from apps.uploadcsv.views.maestro_ups_views import MAESTRO_HIS_UPS_CSV_View, MAESTRO_HIS_UPS_Delete_View, \
    MAESTRO_HIS_UPS_List_View
from apps.uploadcsv.views.verify_data_models_views import VerificarDatosAPIView
from django.urls import path

# ---------------- Data CNV ------------------}

from apps.uploadcsv.views.data_cnv_views import (
    DATA_CNV_CSV_View,
    DATA_CNV_Delete_View,
    DATA_CNV_List_View
)

urls_maestro_actividad = [
    path("upload-csv-maestro_his_actividad_his", MAESTRO_HIS_ACTIVIDAD_HIS_CSV_View.as_view(),
         name="upload-csv-maestro_his_actividad_his"),
    path("delete-all-maestro_his_actividad_his", MAESTRO_HIS_ACTIVIDAD_HIS_Delete_View.as_view(),
         name="delete-all-maestro_his_actividad_his"),
    path("get-all-maestro_his_actividad_his", MAESTRO_HIS_ACTIVIDAD_HIS_List_View.as_view(),
         name="get-all-maestro_his_actividad_his"),


]
urls_centropoblado = [


    path("upload-csv-maestro_his_centro_poblado", MAESTRO_HIS_CENTRO_POBLADO_CSV_View.as_view(),
         name="upload-csv-maestro_his_centro_poblado"),
    path("delete-all-maestro_his_centro_poblado", MAESTRO_HIS_CENTRO_POBLADO_Delete_View.as_view(),
         name="delete-all-maestro_his_centro_poblado"),
    path("get-all-maestro_his_centro_poblado", MAESTRO_HIS_CENTRO_POBLADO_List_View.as_view(),
         name="get-all-maestro_his_centro_poblado")

]

urls_maestro_colegios = [
    path('upload-csv-maestro_his_colegio', MAESTRO_HIS_COLEGIO_CSV_View.as_view(),
         name="upload-csv-maestro_his_colegio"),
    path('delete-all-maestro_his_colegio', MAESTRO_HIS_COLEGIO_Delete_View.as_view(),
         name='delete-all-maestro_his_colegio'),
    path('get-all-maestro_his_colegio', MAESTRO_HIS_COLEGIO_List_View.as_view(),
         name='get-all-maestro_his_colegio'),


]


urls_maestro_condicion_contrato = [
    path('upload-csv-maestro_his_condicion_contrato', MAESTRO_HIS_CONDICION_CONTRATO_CSV_View.as_view(),
         name="upload-csv-maestro_his_condicion_contrato"),
    path('delete-all-maestro_his_condicion_contrato', MAESTRO_HIS_CONDICION_CONTRATO_Delete_View.as_view(),
         name='delete-all-maestro_his_condicion_contrato'),
    path('get-all-maestro_his_condicion_contrato', MAESTRO_HIS_CONDICION_CONTRATO_List_View.as_view(),
         name='get-all-maestro_his_condicion_contrato'),


]

urls_maestro_cpms = [
    path("upload-csv-maestro_his_cie_cpms", MAESTRO_HIS_CIE_CPMS_CSV_View.as_view(),
         name="upload-csv-maestro_his_cie_cpms"),
    path("delete-all-maestro_his_cie_cpms", MAESTRO_HIS_CIE_CPMS_Delete_View.as_view(),
         name="delete-all-maestro_his_cie_cpms"),
    path("get-all-maestro_his_cie_cpms", MAESTRO_HIS_CIE_CPMS_List_View.as_view(),
         name="get-all-maestro_his_cie_cpms"),
]


urls_maestro_tipodoc = [
    path("upload-csv-maestro_his_tipo_doc", MAESTRO_HIS_TIPO_DOC_CSV_View.as_view(),
         name="upload-csv-maestro_his_tipo_doc"),
    path("delete-all-maestro_his_tipo_doc", MAESTRO_HIS_TIPO_DOC_Delete_View.as_view(),
         name="delete-all-maestro_his_tipo_doc"),
    path("get-all-maestro_his_tipo_doc", MAESTRO_HIS_TIPO_DOC_List_View.as_view(),
         name="get-all-maestro_his_tipo_doc"),
]


urls_establecimiento = [
    path("upload-csv-maestro_his_establecimiento", MAESTRO_HIS_ESTABLECIMIENTO_CSV_View.as_view(),
         name="upload-csv-maestro_his_establecimiento"),
    path("delete-all-maestro_his_establecimiento", MAESTRO_HIS_ESTABLECIMIENTO_Delete_View.as_view(),
         name="delete-all-maestro_his_establecimiento"),
    path("get-all-maestro_his_establecimiento", MAESTRO_HIS_ESTABLECIMIENTO_List_View.as_view(),
         name="get-all-maestro_his_establecimiento")
]

urls_etnias = [
    path("upload-csv-maestro_his_etnia", MAESTRO_HIS_ETNIA_CSV_View.as_view(),
         name="upload-csv-maestro_his_etnia"),
    path("delete-all-maestro_his_etnia", MAESTRO_HIS_ETNIA_Delete_View.as_view(),
         name="delete-all-maestro_his_etnia"),
    path("get-all-maestro_his_etnia", MAESTRO_HIS_ETNIA_List_View.as_view(),
         name="get-all-maestro_his_etnia")
]

urls_otra_condicion = [
    path("upload-csv-maestro_his_otra_condicion", MAESTRO_HIS_OTRA_CONDICION_CSV_View.as_view(),
         name="upload-csv-maestro_his_otra_condicion"),
    path("delete-all-maestro_his_otra_condicion", MAESTRO_HIS_OTRA_CONDICION_Delete_View.as_view(),
         name="delete-all-maestro_his_otra_condicion"),
    path("get-all-maestro_his_otra_condicion", MAESTRO_HIS_OTRA_CONDICION_List_View.as_view(),
         name="get-all-maestro_his_otra_condicion")
]

urls_ubigeo = [
    path("upload-csv-maestro_his_ubigeo_inei_reniec", MAESTRO_HIS_UBIGEO_INEI_RENIEC_CSV_View.as_view(),
         name="upload-csv-maestro_his_ubigeo_inei_reniec"),
    path("delete-all-maestro_his_ubigeo_inei_reniec", MAESTRO_HIS_UBIGEO_INEI_RENIEC_Delete_View.as_view(),
         name="delete-all-maestro_his_ubigeo_inei_reniec"),
    path("get-all-maestro_his_ubigeo_inei_reniec", MAESTRO_HIS_UBIGEO_INEI_RENIEC_List_View.as_view(),
         name="get-all-maestro_his_ubigeo_inei_reniec")
]

urls_ups = [
    path("upload-csv-maestro_his_ups", MAESTRO_HIS_UPS_CSV_View.as_view(),
         name="upload-csv-maestro_his_ups"),
    path("delete-all-maestro_his_ups", MAESTRO_HIS_UPS_Delete_View.as_view(),
         name="delete-all-maestro_his_ups"),
    path("get-all-maestro_his_ups", MAESTRO_HIS_UPS_List_View.as_view(),
         name="get-all-maestro_his_ups")
]

urls_financiador = [
    path("upload-csv-maestro_his_financiador", MAESTRO_HIS_FINANCIADOR_CSV_View.as_view(),
         name="upload-csv-financiador"),
    path("delete-all-maestro_his_financiador", MAESTRO_HIS_FINANCIADOR_Delete_View.as_view(),
         name="delete-all-maestro_his_financiador"),
    path("get-all-maestro_his_financiador", MAESTRO_HIS_FINANCIADOR_List_View.as_view(),
         name="get-all-maestro_his_financiador")
]

urls_pais = [
    path("upload-csv-maestro_his_pais", MAESTRO_HIS_PAIS_CSV_View.as_view(),
         name="upload-csv-maestro_his_pais"),
    path("delete-all-maestro_his_pais", MAESTRO_HIS_PAIS_Delete_View.as_view(),
         name="delete-all-maestro_his_pais"),
    path("get-all-maestro_his_pais", MAESTRO_HIS_PAIS_List_View.as_view(),
         name="get-all-maestro_his_pais")
]


# Url relations
urls_maestro_profesion = [
    path("upload-csv-maestro_his_profesion", MAESTRO_HIS_PROFESION_CSV_View.as_view(),
         name="upload-csv-maestro_his_profesion"),
    path("delete-all-maestro_his_profesion", MAESTRO_HIS_PROFESION_Delete_View.as_view(),
         name="delete-all-maestro_his_profesion"),
    path("get-all-maestro_his_profesion", MAESTRO_HIS_PROFESION_List_View.as_view(),
         name="get-all-maestro_his_profesion"),
]


urls_maestro_registrador = [
    path("upload-csv-maestro_his_registrador", MAESTRO_HIS_REGISTRADOR_CSV_View.as_view(),
         name="upload-csv-maestro_his_registrador"),
    path("delete-all-maestro_his_registrador", MAESTRO_HIS_REGISTRADOR_Delete_View.as_view(),
         name="delete-all-maestro_his_registrador"),
    path("get-all-maestro_his_registrador", MAESTRO_HIS_REGISTRADOR_List_View.as_view(),
         name="get-all-maestro_his_registrador"),
]


urls_maestro_personal = [
    path("upload-csv-maestro_his_personal", MAESTRO_HIS_PERSONAL_CSV_View.as_view(),
         name="upload-csv-maestro_his_personal"),
    path("delete-all-maestro_his_personal", MAESTRO_HIS_PERSONAL_Delete_View.as_view(),
         name="delete-all-maestro_his_personal"),
    path("get-all-maestro_his_personal", MAESTRO_HIS_PERSONAL_List_View.as_view(),
         name="get-all-maestro_his_personal"),
]


urls_maestro_paciente = [
    path("upload-csv-maestro_his_paciente", MAESTRO_HIS_PACIENTE_CSV_View.as_view(),
         name="upload-csv-maestro_his_paciente"),
    path("delete-all-maestro_his_paciente", MAESTRO_HIS_PACIENTE_Delete_View.as_view(),
         name="delete-all-paciente"),
    path("get-all-maestro_his_paciente", MAESTRO_HIS_PACIENTE_List_View.as_view(),
         name="get-all-maestro_his_paciente"),
]


# terminado al 90% ,falta algunos detalles de implementacion
urls_maestro_nominal_test = [
    path("upload-csv-maestro_his_nuevo_archivo_plano", MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_CSV_View_TEST.as_view(),
         name="upload-csv-maestro_his_nuevo_archivo_plano"),
    path("delete-all-maestro_his_nuevo_archivo_plano", MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_Delete_View_TEST.as_view(),
         name="delete-all-maestro_his_nuevo_archivo_plano"),
    path("get-all-maestro_his_nuevo_archivo_plano", MAESTRO_HIS_NUEVO_ARCHIVO_PLANO_List_View_TEST.as_view(),
         name="get-all-maestro_his_nuevo_archivo_plano"),
]

# -------- DATA_CNV -----------

urls_data_cnv = [
    path("upload-csv-data_cnv", DATA_CNV_CSV_View.as_view(),
         name="upload-csv-data_cnv"),
    path("delete-all-data_cnv", DATA_CNV_Delete_View.as_view(),
         name="delete-all-data_cnv"),
    path("get-all-data_cnv", DATA_CNV_List_View.as_view(), name="get-all-data_cnv")
]


urls_extra = [
    path("verify-data-models", VerificarDatosAPIView.as_view(),
         name="verify-data-models"),
    path("cnv_relation_paciente", CNV_RELATION_PACIENTEView.as_view(),
         name="cnv_relation_paciente")

]


urlpatterns = urls_maestro_colegios + urls_maestro_tipodoc + \
    urls_maestro_actividad + urls_centropoblado + \
    urls_maestro_condicion_contrato + urls_maestro_cpms + urls_maestro_actividad + urls_centropoblado + urls_establecimiento + \
    urls_etnias + urls_otra_condicion + urls_ubigeo + urls_ups + \
    urls_financiador + urls_pais + urls_maestro_profesion + \
    urls_maestro_registrador + urls_maestro_personal + \
    urls_maestro_paciente + urls_maestro_nominal_test + urls_extra + urls_data_cnv
