from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home/home.html')

def post_view(request):
    return render(request, 'home/post_view.html')

def create_post(request):
    return render(request, 'home/create_post.html')