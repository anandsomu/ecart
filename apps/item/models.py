from django.db import models
from apps.utils.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=500)
    price = models.IntegerField(default=0)

    indexes = [
        models.Index(fields=("name",)),
    ]

    def __str__(self):
        return self.name
