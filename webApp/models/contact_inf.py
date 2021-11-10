from django.db import models

from webApp.models.singleton import SingletonModel

class ContactInfo(SingletonModel, models.Model):
    location = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    website = models.URLField()
    xcod = models.FloatField(null=True, blank=True)
    ycod = models.FloatField(null=True, blank=True)


    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self) -> str:
        return f"{self.location}"