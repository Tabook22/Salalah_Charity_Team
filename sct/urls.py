from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('social.urls')),
    path('admin/', admin.site.urls),
    path('social/', include('social.urls')),
    path('server_update/', include('social.urls')),
]
