from django.shortcuts import render


# Create your views here.
from webApp.models import GalleryImage
from webApp.models.project import Project


def home_page(request):
    context = {
        "home": "active"
    }
    return render(request, "home.html", context)


def projects_page(request):
    projects = Project.objects.all()
    context = {
        "projects": "active",
        "page_title": "Projects",
        "page_subtitle": "Our Secret",
        "banner_image": "2.jpg",
        "projects_list": projects
    }
    return render(request, "projects.html", context)


def gallery_page(request):
    gallery_images = GalleryImage.objects.all()
    context = {
        "gallery": "active",
        "page_title": "Gallery",
        "page_subtitle": "Our Moments",
        "banner_image": "3.jpg",
        "gallery_images": gallery_images
    }
    return render(request, "gallery.html", context)
