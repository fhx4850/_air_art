from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
