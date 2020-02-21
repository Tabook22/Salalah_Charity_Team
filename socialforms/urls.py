from django.urls import path, include
from .views import index
app_name="socialforms"
urlpatterns = [
   path('',index, name="index")
]
