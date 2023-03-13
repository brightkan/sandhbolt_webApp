from django.core.management.base import BaseCommand
from webApp.models import GalleryImage


class Command(BaseCommand):
    help = 'Deletes all gallery images'

    def handle(self, *args, **options):
        # get the path to the pictures directory
        all_images = GalleryImage.objects.all()

        for image in all_images:
            image.delete()

        # Output success message
        self.stdout.write(self.style.SUCCESS('All gallery images successfully deleted'))


