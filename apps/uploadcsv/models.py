
from django.conf import settings
from django.db import models
import codecs


def corregir_codificacion(texto_mal_codificado):
    texto_corregido = codecs.decode(codecs.encode(
        texto_mal_codificado, 'latin1'), 'utf-8')
    return texto_corregido


class MAESTRO_HIS_UBIGEO_INEI_RENIEC(models.Model):
    Id_Ubigueo_Inei = models.BigIntegerField(primary_key=True)
    Id_Ubigueo_Reniec = models.BigIntegerField(null=True, blank=False)
    Departamento = models.CharField(max_length=255, null=True, blank=False)
    Provincia = models.CharField(max_length=255, null=True, blank=False)
    Distrito = models.CharField(max_length=255, null=True, blank=False)
    Codigo_Departamento_Inei = models.IntegerField(null=True, blank=False)
    Codigo_Provincia_Inei = models.IntegerField(null=True, blank=False)
    Codigo_Distrito_Inei = models.IntegerField(null=True, blank=False)
    Codigo_Departamento_Reniec = models.IntegerField(null=True, blank=False)
    Codigo_Provincia_Reniec = models.IntegerField(null=True, blank=False)
    Codigo_Distrito_Reniec = models.IntegerField(null=True, blank=False)

    class Meta:
        verbose_name = 'MAESTRO_HIS_UBIGEO_INEI_RENIEC'
        verbose_name_plural = 'MAESTRO_HIS_UBIGEO_INEI_RENIEC'
        db_table = 'MAESTRO_HIS_UBIGEO_INEI_RENIEC'


class MAESTRO_HIS_ESTABLECIMIENTO(models.Model):
    Id_Establecimiento = models.CharField(max_length=255, primary_key=True)
    Nombre_Establecimiento = models.CharField(
        max_length=255, null=True, blank=True)
    Ubigueo_Establecimiento = models.IntegerField(null=True, blank=True)
    Codigo_Disa = models.IntegerField(null=True, blank=True)
    Disa = models.CharField(max_length=255, null=True, blank=True)
    Codigo_Red = models.IntegerField(null=True, blank=True)
    Red = models.CharField(max_length=255, null=True, blank=True)
    Codigo_MicroRed = models.IntegerField(null=True, blank=True)
    MicroRed = models.CharField(max_length=255, null=True, blank=True)
    Codigo_Unico = models.IntegerField(null=True, blank=True)
    Codigo_Sector = models.IntegerField(null=True, blank=True)
    Descripcion_Sector = models.CharField(
        max_length=255, null=True, blank=True)
    Departamento = models.CharField(max_length=255, null=True, blank=True)
    Provincia = models.CharField(max_length=255, null=True, blank=True)
    Distrito = models.CharField(max_length=255, null=True, blank=True)
    Categoria_Establecimiento = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:

        db_table = 'MAESTRO_HIS_ESTABLECIMIENTO'
        verbose_name_plural = "MAESTRO_HIS_ESTABLECIMIENTO"


class MAESTRO_HIS_CIE_CPMS(models.Model):
    Codigo_Item = models.CharField(max_length=100, primary_key=True)
    Descripcion_Item = models.TextField(null=True, blank=True)
    Fg_Tipo = models.CharField(max_length=255, null=True, blank=True)
    Descripcion_Tipo_Item = models.TextField(null=True, blank=True)
    Fg_Estado = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_CIE_CPMS"
        db_table = "MAESTRO_HIS_CIE_CPMS"


class MAESTRO_HIS_OTRA_CONDICION(models.Model):
    Id_Otra_Condicion = models.CharField(max_length=255, primary_key=True)
    Descripcion_Otra_Condicion = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_OTRA_CONDICION"
        db_table = 'MAESTRO_HIS_OTRA_CONDICION'


class MAESTRO_HIS_ETNIA(models.Model):
    Id_Etnia = models.CharField(max_length=255, primary_key=True)
    Descripcion_Etnia = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_ETNIA"
        db_table = 'MAESTRO_HIS_ETNIA'


class MAESTRO_HIS_COLEGIO(models.Model):
    Id_Colegio = models.AutoField(primary_key=True)

    Descripcion_Colegio = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_COLEGIO"
        db_table = 'MAESTRO_HIS_COLEGIO'


class MAESTRO_HIS_TIPO_DOC(models.Model):
    Id_Tipo_Documento = models.CharField(max_length=255, primary_key=True)
    Abrev_Tipo_Doc = models.CharField(max_length=50, null=True, blank=True)
    Descripcion_Tipo_Documento = models.CharField(
        max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_TIPO_DOC"
        db_table = 'MAESTRO_HIS_TIPO_DOC'


class MAESTRO_HIS_PAIS(models.Model):
    Id_Pais = models.CharField(max_length=100, primary_key=True)
    Descripcion_Pais = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_PAIS"
        db_table = 'MAESTRO_HIS_PAIS'


class MAESTRO_HIS_FINANCIADOR(models.Model):
    Id_Financiador = models.CharField(max_length=255, primary_key=True)
    Descripcion_Financiador = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_FINANCIADOR"
        db_table = 'MAESTRO_HIS_FINANCIADOR'


class MAESTRO_HIS_UPS(models.Model):
    Id_Ups = models.CharField(max_length=255, primary_key=True)
    Descripcion_Ups = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_UPS"
        db_table = 'MAESTRO_HIS_UPS'


class MAESTRO_HIS_ACTIVIDAD_HIS(models.Model):
    Id_Actividad_His = models.CharField(max_length=100, primary_key=True)
    Descripcion_Actividad_His = models.CharField(
        max_length=255, null=True, blank=True)
    Fg_Estado = models.IntegerField()

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_ACTIVIDAD_HIS"
        db_table = 'MAESTRO_HIS_ACTIVIDAD_HIS'


class MAESTRO_HIS_CENTRO_POBLADO(models.Model):
    Id_Centro_Poblado = models.CharField(max_length=255, primary_key=True)
    Descripcion_Centro_Poblado = models.CharField(max_length=255)
    Id_Codigo_Centro_Poblado = models.BigIntegerField(null=True, blank=True)
    Id_Ubigueo_Centro_Poblado = models.BigIntegerField(null=True, blank=True)
    Altitud_Centro_Poblado = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_CENTRO_POBLADO"
        db_table = 'MAESTRO_HIS_CENTRO_POBLADO'


class MAESTRO_HIS_CONDICION_CONTRATO(models.Model):
    Id_Condicion = models.BigIntegerField(primary_key=True)
    Descripcion_Condicion = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_CONDICION_CONTRATO"
        db_table = 'MAESTRO_HIS_CONDICION_CONTRATO'


# -------------------------- modelos con relaciones ------------------------------------------
class MAESTRO_HIS_PROFESION(models.Model):
    Id_Profesion = models.BigIntegerField(primary_key=True)
    Descripcion_Profesion = models.CharField(
        max_length=255, null=True, blank=True)
    Id_Colegio = models.ForeignKey(
        MAESTRO_HIS_COLEGIO, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_PROFESION"
        db_table = 'MAESTRO_HIS_PROFESION'


class MAESTRO_HIS_REGISTRADOR(models.Model):

    Id_Registrador = models.CharField(max_length=255, primary_key=True)
    Id_Tipo_Documento = models.ForeignKey(
        MAESTRO_HIS_TIPO_DOC, on_delete=models.SET_NULL, null=True)

    Numero_Documento = models.CharField(max_length=20, null=True, blank=True)
    Apellido_Paterno_Registrador = models.CharField(
        max_length=50, null=True, blank=True)
    Apellido_Materno_Registrador = models.CharField(
        max_length=50, null=True, blank=True)
    Nombres_Registrador = models.CharField(
        max_length=50, null=True, blank=True)
    Fecha_Nacimiento = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_REGISTRADOR"
        db_table = 'MAESTRO_HIS_REGISTRADOR'


class DATA_CNV(models.Model):
    CNV = models.CharField(max_length=255, primary_key=True)
    Estado = models.CharField(max_length=255, blank=True, null=True)
    CodEESS = models.CharField(max_length=255, blank=True, null=True)
    EESS = models.CharField(max_length=255, blank=True, null=True)
    pApellidoMadre = models.CharField(max_length=255, blank=True, null=True)
    sApellidoMadre = models.CharField(max_length=255, blank=True, null=True)
    nombresMadre = models.CharField(max_length=255, blank=True, null=True)
    Edad = models.IntegerField(blank=True, null=True)
    FecNac = models.CharField(max_length=255, blank=True, null=True)
    Gest_Sem = models.IntegerField(blank=True, null=True)
    TipoDoc = models.CharField(max_length=255, blank=True, null=True)
    Documento = models.CharField(max_length=255, blank=True, null=True)
    Telefono = models.CharField(max_length=255, blank=True, null=True)
    CodEESSPrenatal = models.CharField(max_length=255, blank=True, null=True)
    EESSPrenatal = models.CharField(max_length=255, blank=True, null=True)
    Fecha = models.CharField(max_length=255, blank=True, null=True)
    Hora = models.TimeField(blank=True, null=True)
    Sexo = models.CharField(max_length=255, blank=True, null=True)
    Peso_g = models.FloatField(blank=True, null=True)
    Talla_cm = models.FloatField(blank=True, null=True)
    Apgar = models.FloatField(blank=True, null=True)
    Perimetrocefalico = models.FloatField(blank=True, null=True)
    Perimetrotoracico = models.FloatField(blank=True, null=True)
    Malfcongenita = models.CharField(max_length=255, blank=True, null=True)
    TiempoLigCord = models.CharField(max_length=255, blank=True, null=True)
    Lactanciaprecoz = models.CharField(max_length=255, blank=True, null=True)
    pApellidoProfesional = models.CharField(
        max_length=255, blank=True, null=True)
    sApellidoProfesional = models.CharField(
        max_length=255, blank=True, null=True)
    nombresProfesional = models.CharField(
        max_length=255, blank=True, null=True)
    Profesion = models.CharField(max_length=255, blank=True, null=True)
    NColegio = models.CharField(max_length=255, blank=True, null=True)
    FechaRegistro = models.CharField(max_length=255, blank=True, null=True)
    pApellidoResgistrador = models.CharField(
        max_length=255, blank=True, null=True)
    sApellidoRegistrador = models.CharField(
        max_length=255, blank=True, null=True)
    nombresRegistrador = models.CharField(
        max_length=255, blank=True, null=True)
    tipoPartoId = models.IntegerField(blank=True, null=True)
    tipoParto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "DATA_CNV"
        db_table = 'DATA_CNV'


# tablas con mas de 2 foreign keys


class MAESTRO_HIS_PERSONAL(models.Model):

    Id_Personal = models.CharField(max_length=255, primary_key=True)

    Id_Tipo_Documento = models.ForeignKey(
        MAESTRO_HIS_TIPO_DOC, on_delete=models.SET_NULL, null=True)

    Numero_Documento = models.CharField(max_length=50, null=True, blank=True)
    Apellido_Paterno_Personal = models.CharField(
        max_length=50, null=True, blank=True)
    Apellido_Materno_Personal = models.CharField(
        max_length=50, null=True, blank=True)
    Nombres_Personal = models.CharField(max_length=50, null=True, blank=True)
    Fecha_Nacimiento = models.CharField(max_length=255, null=True, blank=True)

    Id_Condicion = models.ForeignKey(
        MAESTRO_HIS_CONDICION_CONTRATO, on_delete=models.SET_NULL, null=True)
    Id_Profesion = models.ForeignKey(
        MAESTRO_HIS_PROFESION, on_delete=models.SET_NULL, null=True)
    Id_Colegio = models.ForeignKey(
        MAESTRO_HIS_COLEGIO, on_delete=models.SET_NULL, null=True)
    Id_Establecimiento = models.ForeignKey(
        MAESTRO_HIS_ESTABLECIMIENTO, on_delete=models.SET_NULL, null=True)

    Numero_Colegiatura = models.CharField(
        max_length=255, null=True, blank=True)
    Fecha_Alta = models.CharField(max_length=255, null=True, blank=True)
    Fecha_Baja = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_PERSONAL"
        db_table = 'MAESTRO_HIS_PERSONAL'


class MAESTRO_HIS_PACIENTE(models.Model):

    Id_Paciente = models.CharField(
        primary_key=True, unique=True, max_length=255)

    Id_Tipo_Documento = models.ForeignKey(
        MAESTRO_HIS_TIPO_DOC, on_delete=models.SET_NULL, null=True)

    Numero_Documento = models.CharField(max_length=255, null=True, blank=True)
    Apellido_Paterno_Paciente = models.CharField(max_length=255, null=True)
    Apellido_Materno_Paciente = models.CharField(max_length=255, null=True)
    Nombres_Paciente = models.CharField(max_length=255, null=True)
    Fecha_Nacimiento = models.CharField(max_length=255, null=True)
    Genero = models.CharField(max_length=255, null=True, blank=True)

    Id_Etnia = models.ForeignKey(
        MAESTRO_HIS_ETNIA, on_delete=models.SET_NULL, null=True)

    Historia_Clinica = models.CharField(max_length=255, null=True)
    Ficha_Familiar = models.CharField(max_length=255, null=True)
    Ubigeo_Nacimiento = models.IntegerField(null=True)
    Ubigeo_Reniec = models.IntegerField(null=True)
    Domicilio_Reniec = models.CharField(max_length=255, null=True)
    Ubigeo_Declarado = models.IntegerField(null=True)
    Domicilio_Declarado = models.IntegerField(null=True)
    Referencia_Domicilio = models.IntegerField(null=True)

    Id_Pais = models.ForeignKey(
        MAESTRO_HIS_PAIS, on_delete=models.SET_NULL, null=True)
    Id_Establecimiento = models.ForeignKey(
        MAESTRO_HIS_ESTABLECIMIENTO, on_delete=models.SET_NULL, null=True)

    Fecha_Alta = models.CharField(max_length=255, null=True)
    Fecha_Modificacion = models.CharField(max_length=255, null=True)
    # CNV = models.ForeignKey(
    #    DATA_CNV, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_PACIENTE"
        db_table = 'MAESTRO_HIS_PACIENTE'


# ________________________________ Principal Nominal ______________________________________________________

class MAESTRO_HIS_NUEVO_ARCHIVO_PLANO(models.Model):
    Id = models.IntegerField(primary_key=True)
    Id_Cita = models.CharField(max_length=255, null=True)
    Anio = models.IntegerField(null=True, blank=True)
    Mes = models.IntegerField(null=True, blank=True)
    Dia = models.IntegerField(null=True, blank=True)
    Fecha_Atencion = models.CharField(max_length=255, null=True, blank=True)
    Lote = models.CharField(max_length=255, null=True, blank=True)
    Num_Pag = models.IntegerField(null=True, blank=True)
    Num_Reg = models.IntegerField(null=True, blank=True)

    Id_Ups = models.ForeignKey(
        MAESTRO_HIS_UPS, on_delete=models.SET_NULL, null=True)

    Id_Establecimiento = models.ForeignKey(
        MAESTRO_HIS_ESTABLECIMIENTO, on_delete=models.SET_NULL, null=True)

    Id_Paciente = models.ForeignKey(
        MAESTRO_HIS_PACIENTE,  on_delete=models.SET_NULL, null=True)
    Id_Personal = models.ForeignKey(
        MAESTRO_HIS_PERSONAL, on_delete=models.SET_NULL, null=True)

    Id_Registrador = models.ForeignKey(
        MAESTRO_HIS_REGISTRADOR,  on_delete=models.SET_NULL, null=True)

    Id_Financiador = models.ForeignKey(
        MAESTRO_HIS_FINANCIADOR,
        on_delete=models.SET_NULL, null=True

    )

    Id_Condicion_Establecimiento = models.CharField(
        max_length=255, null=True, blank=True)

    Id_Condicion_Servicio = models.CharField(
        max_length=255, null=True, blank=True)

    Edad_Reg = models.IntegerField(null=True, blank=True)
    Tipo_Edad = models.CharField(max_length=255, null=True, blank=True)
    Anio_Actual_Paciente = models.IntegerField(null=True, blank=True)
    Mes_Actual_Paciente = models.IntegerField(null=True, blank=True)
    Dia_Actual_Paciente = models.IntegerField(null=True, blank=True)

    Id_Turno = models.CharField(max_length=255,  null=True, blank=True)

    Codigo_Item = models.ForeignKey(
        MAESTRO_HIS_CIE_CPMS,  on_delete=models.SET_NULL, null=True)

    Tipo_Diagnostico = models.CharField(max_length=255, null=True, blank=True)

    Peso = models.FloatField(null=True, blank=True)
    Talla = models.FloatField(null=True, blank=True)
    Hemoglobina = models.FloatField(null=True, blank=True)
    Perimetro_Abdominal = models.FloatField(null=True, blank=True)
    Perimetro_Cefalico = models.FloatField(null=True, blank=True)

    Id_Otra_Condicion = models.ForeignKey(
        MAESTRO_HIS_OTRA_CONDICION, on_delete=models.SET_NULL, null=True)

    Id_Centro_Poblado = models.ForeignKey(
        MAESTRO_HIS_CENTRO_POBLADO,
        on_delete=models.SET_NULL, null=True
    )
    Id_Correlativo = models.IntegerField(null=True, blank=True)
    Id_Correlativo_Lab = models.IntegerField(null=True, blank=True)
    Valor_Lab = models.CharField(max_length=255, null=True, blank=True)
    Fecha_Ultima_Regla = models.CharField(max_length=255, null=True)
    Fecha_Solicitud_Hb = models.CharField(max_length=255, null=True)
    Fecha_Resultado_Hb = models.CharField(max_length=255, null=True)
    Fecha_Registro = models.CharField(max_length=255, null=True)
    Fecha_Modificacion = models.CharField(max_length=255, null=True)

    Id_Pais = models.ForeignKey(
        MAESTRO_HIS_PAIS,
        on_delete=models.SET_NULL, null=True

    )

    class Meta:
        verbose_name_plural = "MAESTRO_HIS_NUEVO_ARCHIVO_PLANO"
        verbose_name_plural = "MAESTRO_HIS_NUEVO_ARCHIVO_PLANO"
        db_table = 'MAESTRO_HIS_NUEVO_ARCHIVO_PLANO'


# Plugins Extras
