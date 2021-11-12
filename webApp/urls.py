from django.urls import path
import webApp.views as views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('projects/', views.projects_page, name="projects_page"),
    path('gallery/', views.gallery_page, name="gallery_page"),
    path('services/', views.services_page, name="services_page"),
    path('about/', views.about_page, name="about_page"),
    path('contact/', views.contact_page, name="contact_page"),
]




