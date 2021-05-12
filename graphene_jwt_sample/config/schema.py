# parent project level schema which combines all app level schemas

import graphene
import graphql_jwt

from ..graphql import transportation


class Query(
        transportation.schema.Query,
        graphene.ObjectType):
    ...
    # debug = graphene.Field(DjangoDebug, name='_debug')


# class Mutation(
#         Accounts.schema.Mutation,
#         testtypes.schema.Mutation,
#         questiontypes.schema.Mutation,
#         userstats.schema.Mutation,
#         knowledgepoint.schema.Mutation,
#         graphene.ObjectType):

#     # The token opreate that graphql_jwt support.
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()
#     revoke = graphql_jwt.Revoke.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
