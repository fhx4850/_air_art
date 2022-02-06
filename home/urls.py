from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/', views.post_view, name='post'),
    path('create-new-post/', views.create_post, name="create_post"),
]
