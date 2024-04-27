
from datetime import datetime  
from apps.user.serializers import ProfileSerializer, UserAccountSerializer
from .models import UserAccount,Profile
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
import cloudinary
import cloudinary.uploader
from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailView(APIView):
    def get(self, request,format=None):
        user = request.user
        user_data = UserAccountSerializer(user).data
        profile = request.user.profile
        profile_data = ProfileSerializer(profile).data
        detailuser = {}
        detailuser.update(user_data)
        detailuser.update(profile_data)
        
        return Response(detailuser)


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
            users = User.objects.exclude(nickname="admin")
            serializer = UserAccountSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class UpdateNicknameView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_nickname = request.data.get('nickname', None)
        if new_nickname:
            try:
                user.nickname = new_nickname
                user.save()
                return Response({'message': 'Nickname updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Nickname field is required'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateFirstNameView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_first_name = request.data.get('first_name', None)
        if new_first_name:
            try:
                user.first_name = new_first_name
                user.save()
                return Response({'message': 'First name updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'First name field is required'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateLastNameView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_last_name = request.data.get('last_name', None)
        if new_last_name:
            try:
                user.last_name = new_last_name
                user.save()
                return Response({'message': 'Last name updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Last name field is required'}, status=status.HTTP_400_BAD_REQUEST)

class UpdatePhotoUrlView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_photo = request.FILES.get('photo', None)
        
        if new_photo:
            try:
                # Subir imagen a Cloudinary
                uploaded_photo = cloudinary.uploader.upload(new_photo)
                
                # Actualizar URL de la foto en el modelo de usuario
                user.photo_url = uploaded_photo['secure_url']
                user.save()
                
                return Response({'message': 'Photo updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Photo field is required'}, status=status.HTTP_400_BAD_REQUEST)



class UpdateLocationView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_location = request.data.get('location', None)
        if new_location:
            try:
                user.location = new_location
                user.save()
                return Response({'message': 'Location updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Location field is required'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateBirthdateView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_birthdate_str = request.data.get('birthdate', None)
        
        if new_birthdate_str is not None:
            try:
                new_birthdate = datetime.strptime(new_birthdate_str, '%Y-%m-%d').date()
                # Obtener el perfil del usuario actual
                profile, created = Profile.objects.get_or_create(user=user)
                profile.birthdate = new_birthdate
                profile.save()
                return Response({'message': 'Birthdate updated successfully'}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Birthdate field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UpdatePhoneNumberView(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        new_phone_number = request.data.get('phone_number', None)
        if new_phone_number:
            try:
                profile, created = Profile.objects.get_or_create(user=user)
                profile.phone_number = new_phone_number
                profile.save()
                return Response({'message': 'Phone number updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Phone number field is required'}, status=status.HTTP_400_BAD_REQUEST)




class UserAccountActivationDeactivationView(APIView):    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        email = request.data.get('email')
        is_activate = request.data.get('is_activate', True)
        current_user = request.user
        try:
            user = User.objects.get(email=email)
            if is_activate and not current_user.is_staff:
                return Response({'error': 'Solo un administrador puede activar una cuenta.'}, status=403)            
            if user == current_user and is_activate:
                return Response({'error': 'No puedes activar tu propia cuenta.'}, status=403)
            user.is_active = is_activate
            user.save()
            if is_activate:
                message = 'Se ha activado la cuenta.'
            else:
                message = 'Se ha desactivado la cuenta.'
            return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'No se encontró ningún usuario con ese correo electrónico.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
