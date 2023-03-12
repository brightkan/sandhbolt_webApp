from django.core.management.base import BaseCommand
from webApp.models import GalleryImage


class Command(BaseCommand):
    help = 'Re-saves all GalleryImage instances to generate new thumbnails'

    def handle(self, *args, **options):
        # Retrieve all instances of GalleryImage
        all_images = GalleryImage.objects.all()

        # Re-save each instance to generate new thumbnails
        for image in all_images:
            image.save()

        # Output success message
        self.stdout.write(self.style.SUCCESS('Successfully re-saved all GalleryImage instances'))
