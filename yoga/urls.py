
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.context_processors import media
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('health.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('health.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

