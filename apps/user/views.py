

from apps.user.serializers import UserAccountSerializer
from .models import UserAccount
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from apps.user.models import UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()


class DeleteUserView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request):

        OutstandingToken.objects.all().delete()
        UserAccount.objects.all().delete()

        return Response({"mensaje": "Todos los usuarios eliminados"}, status=204)


class UserAccountListView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        try:
            users = User.objects.exclude(nickname="Admin")
            serializer = UserAccountSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class UserAccountDeactivatePermissionView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            user.desactivate_account = True
            user.save()
            return Response({'message': 'Se le denego el permiso'}, status=status.HTTP_204_NO_CONTENT)

        except UserAccount.DoesNotExist:
            return Response({'error': 'No se encontró ningún usuario con ese correo electrónico.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class UserAccountReactivatePermissionView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            user.desactivate_account = False
            user.save()
            return Response({'message': 'Se le otorgo el permiso'}, status=status.HTTP_204_NO_CONTENT)
        except UserAccount.DoesNotExist:
            return Response({'error': 'No se encontró ningún usuario con ese correo electrónico.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
