from django.contrib import admin

from webApp.models.gallery_image import GalleryImage
from webApp.models.slider_image import SliderImage
from webApp.models.project import Project
from webApp.models.review import Review
from webApp.models.client import Client
from webApp.models.social_media_links import SocialMediaLink
from webApp.models.company_profile import CompanyProfile
from webApp.models.contact_inf import ContactInfo

# Register your models here.
admin.site.register(CompanyProfile)
admin.site.register(ContactInfo)
admin.site.register(SocialMediaLink)
admin.site.register(Client)
admin.site.register(Review)
admin.site.register(Project)
admin.site.register(SliderImage)
admin.site.register(GalleryImage)
