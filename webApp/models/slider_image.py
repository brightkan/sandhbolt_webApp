import os

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import SET_NULL

from webApp.models.company_profile import CompanyProfile


def create_path_slider_image(instance, filename):
    if instance.picture:
        try:
            existing_slider_image = SliderImage.objects.get(pk=instance.id)
            existing_slider_image.picture.delete()
        except ObjectDoesNotExist:
            pass

    return os.path.join("company_profile", "slider_images", filename)


class SliderImage(models.Model):
    company = models.ForeignKey(CompanyProfile, default=1, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=create_path_slider_image, null=False)

    def __str__(self):
        return f"{self.title}"

    def delete(self, using=None, keep_parents=False):
        try:
            self.picture.delete()
        except ObjectDoesNotExist:
            pass
        super().delete()
