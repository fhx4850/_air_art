from django.shortcuts import render


def profile(request):
    return render(request, 'site_profile/profile.html')