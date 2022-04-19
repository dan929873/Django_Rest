from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet


from todo.models import Project, TODO
from todo.serializers import ProjectModelSerializer, TODOModelSerializer

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Project.objects.filter(name__contains=name)
        return Project.objects.all()




class TODOModelViewSet(ModelViewSet):
    serializer_class = TODOModelSerializer
    queryset = TODO.objects.all()
    pagination_class = TODOLimitOffsetPagination

    def get_queryset(self):
        project = self.request.query_params.get('project', None)
        if project:
            return TODO.objects.filter(name__contains=project)
        return TODO.objects.all()

    def perform_destroy(self, instance):
        instance.activ = False
        instance.save()



