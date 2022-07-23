from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads.views import index
from rest_framework import routers
from users.views import LocationViewSet


router = routers.SimpleRouter()
router.register('loc', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('index/', index),
    path('', include("ads.urls")),
    path('user/', include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
