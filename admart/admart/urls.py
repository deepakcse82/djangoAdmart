
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adweb.urls')),
    path('backend_mart/', include('adadmin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
