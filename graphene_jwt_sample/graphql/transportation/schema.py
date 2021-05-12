# parent project level schema which combines all app level schemas

import graphene
import graphql_jwt

from ...transportation import models
from .types import MotoConnection, MotoType


class transportationQueries(graphene.ObjectType):
    moto = graphene.Field(MotoType,
        id=graphene.Argument(graphene.ID, description="ID of the attribute."),)
    motos = graphene.ConnectionField(MotoConnection)

    # moto = graphene.Field(MotoType,
    #     id=graphene.Argument(graphene.ID, description="ID of the attribute."),)
    # motos = graphene.ConnectionField(MotoConnection)


    def resolve_moto(self, info, id):
        return graphene.Node.get_node_from_global_id(info, id, MotoType)
        

    def resolve_motos(self, info):
        return models.moto.objects.all()