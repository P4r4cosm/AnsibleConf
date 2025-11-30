from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import socket

def home(request):
    return HttpResponse(f"Hello from Kubernetes! Hostname: {socket.gethostname()}")

def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('health/', health),
    path('', include('django_prometheus.urls')),
]
