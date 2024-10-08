from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from  apps.user.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAcountCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User

        fields = '__all__'


class UserAccountSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User

        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
            
        model =Profile
        fields = '__all__'



        
