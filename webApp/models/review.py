from django.db import models
from django.db.models import SET_NULL

from webApp.models.client import Client


class Review(models.Model):
    person_name = models.CharField(max_length=40)
    rating = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    client = models.OneToOneField(Client, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"{self.person_name}"
