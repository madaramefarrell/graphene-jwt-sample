import os

from django.utils.timezone import now
from graphql_jwt.settings import jwt_settings


def jwt_payload(user, context=None):
    # PyJWT didn't support jti, scope and some others claims.
    # They think those things will handle by developers themselves.
    # So, when the time we need the claims, we have to add them by ourselves.

    scope = []
    typ = "JWS"
    iss = "graphene_jwt_sample"
    jwt_expires = (now() + jwt_settings.JWT_EXPIRATION_DELTA).timestamp() if jwt_settings.JWT_EXPIRATION_DELTA else None

    payload = {
        'sub': str(user.id),
        'username': user.username,
        'iss': iss,
        'typ': typ,
        'scope': scope,
        'iat': now().timestamp(),
        'exp': jwt_expires,
    }

    if scope == []:
        payload['scope'] += ["*"]

    return payload
