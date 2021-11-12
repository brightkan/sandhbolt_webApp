from PIL import Image
size = 120,120
for num in range(1,69):
    im = Image.open(f"../galleryImages/{num}.jpg", "r")
    new_image = im.resize((400, 400))
    new_image.thumbnail(size)
    new_image.save("../gallerythumbnails/%s.jpg" % (num))
