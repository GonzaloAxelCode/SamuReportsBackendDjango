from django.db import connection


def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.callproc('public.sp_condicion_pacientes')
        results = cursor.fetchall()
        field_names = [name[0] for name in cursor.description]
        return [dict(zip(field_names, result)) for result in results]


def my_custom_sql2():
    with connection.cursor() as cursor:
        cursor.callproc('public.obtener_indicador_errornr')
        results = cursor.fetchall()
        field_names = [name[0] for name in cursor.description]
        return [dict(zip(field_names, result)) for result in results]
