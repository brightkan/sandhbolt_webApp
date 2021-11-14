from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from sandhbolt import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("webApp.urls"))
]

handler404 = "webApp.views._404_page"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
