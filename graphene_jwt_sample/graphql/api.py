import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug
from graphene_federation import build_schema

from .account.schema import accountQueries
from .transportation.schema import transportationQueries


class Query(transportationQueries, accountQueries,graphene.ObjectType):

    debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(graphene.ObjectType):
    
    # The token operate that graphql_jwt support.
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke = graphql_jwt.Revoke.Field()


schema = build_schema(Query, mutation=Mutation)
