from django.db import models
from django.db.models.deletion import SET_NULL
from webApp.models.social_media_links import SocialMediaLink

from webApp.models.singleton import SingletonModel
from webApp.models.contact_inf import ContactInfo


class CompanyProfile(SingletonModel, models.Model):
    name = models.CharField(max_length=20)
    since = models.IntegerField()
    vision = models.TextField()
    mission = models.TextField()
    about = models.TextField()
    logo = models.FileField()
    profile_pdf = models.FileField(blank=False)
    contact_info = models.OneToOneField(ContactInfo, on_delete=SET_NULL, null=True)
    social_media_links = models.OneToOneField(SocialMediaLink, on_delete=SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"

    def __str__(self) -> str:
        return f"{self.name}"