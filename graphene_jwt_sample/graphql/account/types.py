import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):

    class Meta:
        model = User
        interfaces = (graphene.Node, )

class UserConnection(graphene.Connection):
    class Meta:
        node = UserType