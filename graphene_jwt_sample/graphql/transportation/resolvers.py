from ...transportation import models


def resolve_motos(info, **_kwargs):
    return models.moto.objects.all()
