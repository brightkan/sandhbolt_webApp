from PIL import Image

figures = ''
for num in range(1, 69):
    image = Image.open(f"../galleryImages/{num}.jpg")
    width, height = image.size
    figures = figures + f'<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">\
        <a href="/images/galleryImages/{num}.jpg" itemprop="contentUrl" data-size="{width}x{height}">\
        <img src="/images/gallerythumbnails/{num}.jpg" itemprop="thumbnail" alt="Image description" />\
        </a>\
        <figcaption itemprop="caption description">Image caption  1</figcaption></figure>'


hs = open("gallery_figures.html", 'w')
hs.write(figures)
