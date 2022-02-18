import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<slug:slug>/', views.ProfileDetail.as_view(), name='profile'),
    path('profile/<slug:slug>/edit', views.UpdateProfile.as_view(), name="profileUpdate"),
    path('follow/', views.FollowList.as_view(), name='follows'),
    path('profile/folders-update/<slug:slug>/', views.FolderUpdate.as_view(), name='folder_update'),
]
