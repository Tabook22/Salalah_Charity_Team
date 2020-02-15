from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"social/index.html")

def server_update(request):
    return HttpResponse("<h1>In the Name of God most Merci most Mercifull</h1>")
