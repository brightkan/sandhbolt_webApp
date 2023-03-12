import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sandhbolt.settings')

# Initialize Django
django.setup()

from webApp.models import GalleryImage

# Retrieve all instances of GalleryImage
all_images = GalleryImage.objects.all()

# Re-save each instance to generate new thumbnails
for image in all_images:
    image.save()
