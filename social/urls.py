from django.urls import path
from .views import index
app_name = "social"

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
]
