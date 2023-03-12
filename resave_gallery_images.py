from webApp.models import GalleryImage

# Retrieve all instances of GalleryImage
all_images = GalleryImage.objects.all()

# Re-save each instance to generate new thumbnails
for image in all_images:
    image.save()
