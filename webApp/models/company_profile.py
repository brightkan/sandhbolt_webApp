import os

from django.db import models
from django.db.models.deletion import SET_NULL
from webApp.models.social_media_links import SocialMediaLink

from webApp.models.singleton import SingletonModel
from webApp.models.contact_inf import ContactInfo


def create_path_logo(instance, filename):
    existing_company_profile = CompanyProfile.load()
    if instance.logo:
        try:
            existing_company_profile.logo.delete()
        except FileNotFoundError:
            pass

    return os.path.join("company_profile", filename)


def create_path_pdf(instance, filename):
    existing_company_profile = CompanyProfile.load()
    if instance.profile_pd:
        try:
            existing_company_profile.profile_pdf.delete()
        except FileNotFoundError:
            pass
    return os.path.join("company_profile", filename)


class CompanyProfile(SingletonModel, models.Model):
    name = models.CharField(
        max_length=20,
        default="Sandhbolt"
    )
    since = models.IntegerField(default=2015)
    vision = models.TextField(null=True)
    mission = models.TextField(null=True)
    about = models.TextField(null=True)
    logo = models.ImageField(upload_to=create_path_logo, null=True)
    profile_pdf = models.FileField(blank=False, null=True)
    contact_info = models.OneToOneField(ContactInfo, on_delete=SET_NULL, null=True)
    social_media_links = models.OneToOneField(SocialMediaLink, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"

    def __str__(self) -> str:
        return f"{self.name}"
