from django.contrib.auth.models import User
from django.db import models


class transportation(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.IntegerField()
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        abstract = True


class car(transportation):

    def __str__(self):
        return f"No. {self.id} {self.name}"


class moto(transportation):
    has_abs = models.BooleanField(default=False)

    def __str__(self):
        return f"No. {self.id} {self.name}"
