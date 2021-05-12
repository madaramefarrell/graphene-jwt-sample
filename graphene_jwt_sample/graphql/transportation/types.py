import graphene
from graphene_django import DjangoObjectType

from ...transportation import models


class MotoType(DjangoObjectType):

    class Meta:
        model = models.moto
        interfaces = (graphene.Node, )

class MotoConnection(graphene.Connection):
    class Meta:
        node = MotoType