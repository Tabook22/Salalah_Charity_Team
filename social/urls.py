from django.urls import path
from .views import index,server_update
app_name = "social"

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
    path('sup/', server_update),
]
