import os

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import base64
from io import BytesIO
from PIL import Image


def create_path_gallery_image(instance, filename):
    if instance.picture:
        try:
            existing_slider_image = GalleryImage.objects.get(pk=instance.id)
            existing_slider_image.picture.delete()
        except ObjectDoesNotExist:
            pass

    return os.path.join("gallery_images", filename)


class GalleryImage(models.Model):
    caption = models.CharField(max_length=100, default="Civil Engineering")
    picture = models.ImageField(upload_to=create_path_gallery_image)
    thumbnail = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.caption}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.picture:
            self.thumbnail = None
        else:
            thumbnail_size = 120, 120
            data_img = BytesIO()
            tiny_img = Image.open(self.picture)
            tiny_img.thumbnail(thumbnail_size)
            tiny_img.save(data_img, format="BMP")
            tiny_img.close()
            try:
                self.thumbnail = "data:image/jpg;base64,{}".format(
                    base64.b64encode(data_img.getvalue()).decode("utf-8")
                )
            except UnicodeDecodeError:
                pass

        super(GalleryImage, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        try:
            self.picture.delete()
            self.thumbnail.delete()
        except ObjectDoesNotExist:
            pass
        super().delete()
