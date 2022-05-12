from rest_framework.serializers import ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserModelSerializerV2(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
