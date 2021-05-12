# parent project level schema which combines all app level schemas

import graphene
import graphql_jwt
from django.contrib.auth.models import User

from .types import UserConnection, UserType


class accountQueries(graphene.ObjectType):
    user = graphene.Field(UserType,id=graphene.Argument(graphene.ID, description="ID of the attribute."))
    users = graphene.ConnectionField(UserConnection)

    def resolve_user(self, info, id):
        return graphene.Node.get_node_from_global_id(info, id, UserType)

    def resolve_users(self, info):
        return User.objects.all()