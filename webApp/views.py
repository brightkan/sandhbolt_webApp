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


def services_page(request):
    context = {
        "services": "active",
        "page_title": "Services",
        "page_subtitle": "What we do?",
        "banner_image": "4.jpg",
    }
    return render(request, "services.html", context)


def about_page(request):
    context = {
        "about": "active",
        "page_title": "About Us",
        "page_subtitle": "Company Info",
        "banner_image": "5.jpg",
    }
    return render(request, "about.html", context)


def contact_page(request):
    context = {
        "contact": "active",
        "page_title": "Contact Us",
        "page_subtitle": "Get in Touch",
        "banner_image": "5.jpg",
    }
    return render(request, "contact.html", context)


def _404_page(request, exception):
    context = {
        "_404_page": "active",
        "page_title": "Page Not Found",
        "page_subtitle": "404",
        "banner_image": "5.jpg",
    }
    return render(request, "404.html", context)
