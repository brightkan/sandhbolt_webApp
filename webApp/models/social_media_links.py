from django.db import models

from webApp.models.singleton import SingletonModel


class SocialMediaLink(SingletonModel, models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Social Media Links"
        verbose_name_plural = "Social Media Links"
