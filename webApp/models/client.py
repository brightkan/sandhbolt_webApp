from django.db import models


class Client(models.Model):
    logo = models.FileField(blank=True, null=True)
    name = models.CharField(max_length=30)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
