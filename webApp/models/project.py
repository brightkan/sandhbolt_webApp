from django.db import models
from webApp.models import Client


class Project(models.Model):
    title = models.CharField(max_length=40)
    started = models.DateField()
    ended = models.DateField(null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=20)
    role = models.CharField(max_length=40)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self):
        return f"{self.title}"
