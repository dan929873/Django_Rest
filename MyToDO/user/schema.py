import graphene
from graphene_django import DjangoObjectType

from todo.models import Project, TODO
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class TodoType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    def resolve_all_users(self, info):
        return User.objects.all()

    all_projets = graphene.List(ProjectType)
    def resolve_all_projets(self, info):
        return Project.objects.all()

    all_todo = graphene.List(TodoType)
    def resolve_all_todo(self, info):

        return TODO.objects.all()

class UserMutation(graphene.Mutation):
    class Arguments:
        is_active = graphene.Boolean(required=True)
        id = graphene.ID()
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, is_active, id):
        user = User.objects.get(pk=id)
        user.is_active = is_active
        user.save()
        return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
