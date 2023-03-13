import os
from django.core.files import File
from django.core.management.base import BaseCommand
from webApp.models import GalleryImage


class Command(BaseCommand):
    help = 'Imports pictures from pictures folder to GalleryImage'

    def handle(self, *args, **options):
        # get the path to the pictures directory
        pictures_dir = os.path.join(os.getcwd(), 'pictures')

        # get a list of all image files in the directory
        image_files = [os.path.join(pictures_dir, f) for f in os.listdir(pictures_dir) if
                       f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

        # create a GalleryImage instance for each image file
        for image_file in image_files:
            with open(image_file, 'rb') as f:
                # create a new GalleryImage instance
                gallery_image = GalleryImage(caption=os.path.basename(image_file))

                # set the picture field using Django's File object
                gallery_image.picture.save(os.path.basename(image_file), File(f))

                # save the instance
                gallery_image.save()


