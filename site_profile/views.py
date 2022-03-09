from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, ListView
from .models import FollowModel, Profile, Folder
from .forms import UpdateProfileForm
from services.BaseServiceMixin import BaseServiceMixin

class ProfileDetail(BaseServiceMixin, DetailView):
    model = Profile
    template_name = 'site_profile/profile.html'
    context_object_name = 'profile'
    slug_field = 'profile_slug_url'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            id = request.POST.get('follow_id')
            self.create_follow(request, id)
            return HttpResponse('follow')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prof = Profile.objects.get(profile_slug_url=self.get_detailview_instance_slug(self))
        context["folders"] = Folder.objects.filter(folder_profile=prof)
        return context
        
class UpdateProfile(BaseServiceMixin, UpdateView):
    model = Profile
    context_object_name = 'profile'
    form_class = UpdateProfileForm
    template_name = 'site_profile/profile_edit.html'
    slug_field = 'profile_slug_url'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = UpdateProfileForm(request.POST, request.FILES)
            if form.is_valid():
                self.update_profile(request)
            if 'creeate_folder' in request.POST:
                self.create_folder(request)
            return redirect('profile', self.get_detailview_instance_slug(self))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folders"] = Folder.objects.filter(folder_profile=self.get_current_profile(self.request))
        return context
    


class FollowList(BaseServiceMixin, ListView):
    model = FollowModel
    template_name = 'site_profile/follow.html'
    context_object_name = 'follows'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            id = request.POST.get('unfollow_id')
            self.create_follow(request, id)
            return HttpResponse('Follow')


class FolderUpdate(BaseServiceMixin, UpdateView):
    model = Folder
    template_name = 'site_profile/folder_update.html'
    context_object_name = 'folder'
    fields = ('folder_name', 'folder_bg')
    slug_field = 'folder_url'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.update_folder(request)
            return redirect('profile', self.get_current_profile(request).profile_slug_url)