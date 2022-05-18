import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class Query(graphene.ObjectType):
    all_user = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)
