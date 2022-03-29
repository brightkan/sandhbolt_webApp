import os

from PIL import Image
folder_name = "pictures"

for pic in os.listdir(folder_name):
    filename = os.path.join(folder_name, pic)
    with Image.open(filename) as im:
        Gallery.objects.create(

        )
