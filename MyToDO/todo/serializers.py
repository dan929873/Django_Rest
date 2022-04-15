from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TODO, Project


class TODOModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'

class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'