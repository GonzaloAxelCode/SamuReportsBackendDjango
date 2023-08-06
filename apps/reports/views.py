import time
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.reports.utils import my_custom_sql, my_custom_sql2


class MyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        start_time = time.time()
        data = my_custom_sql()
        end_time = time.time()

        response_data = {
            "message": "data exitosa",
            "time": end_time - start_time,
            "results": data
        }

        return Response(response_data)


class MyView2(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        start_time = time.time()
        data = my_custom_sql2()

        end_time = time.time()

        response_data = {
            "message": "data exitosa",
            "time": end_time - start_time,
            "results": data
        }

        return Response(response_data)
