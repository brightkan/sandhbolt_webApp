from django.db import models
from webApp.models import Client


class Project(models.Model):
    year = models.CharField(max_length=4)
    description = models.TextField()
    location = models.CharField(max_length=20)
    role = models.CharField(max_length=40)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-year']
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.role}"
