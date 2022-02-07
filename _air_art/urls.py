from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('profile/', include('site_profile.urls')),
    path('accounts/', include('allauth.urls')),
]
