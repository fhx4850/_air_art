from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView, ListView
from flask import request
from .models import FollowModel, Profile, Folder
from .forms import UpdateProfileForm


def profile(request):
    return render(request, 'site_profile/profile.html')


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'site_profile/profile.html'
    context_object_name = 'profile'
    slug_field = 'profile_slug_url'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            id = request.POST.get('follow_id')
            create_follow(request, id)
            return HttpResponse('follow')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prof = Profile.objects.get(profile_slug_url=get_detailview_instance_slug(self))
        context["folders"] = Folder.objects.filter(folder_profile=prof)
        return context
    
        
        
class UpdateProfile(UpdateView):
    model = Profile
    context_object_name = 'profile'
    form_class = UpdateProfileForm
    template_name = 'site_profile/profile_edit.html'
    slug_field = 'profile_slug_url'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = UpdateProfileForm(request.POST, request.FILES)
            if form.is_valid():
                update_profile(request)
            if 'creeate_folder' in request.POST:
                create_folder(request)
            return redirect('profile', get_detailview_instance_slug(self))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folders"] = Folder.objects.filter(folder_profile=get_current_profile(self.request))
        return context
    


class FollowList(ListView):
    model = FollowModel
    template_name = 'site_profile/follow.html'
    context_object_name = 'follows'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            id = request.POST.get('unfollow_id')
            # print(id)
            create_follow(request, id)
            return HttpResponse('Follow')


class FolderUpdate(UpdateView):
    model = Folder
    template_name = 'site_profile/folder_update.html'
    context_object_name = 'folder'
    fields = ('folder_name', 'folder_bg')
    slug_field = 'folder_url'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            update_folder(request)
            return redirect('profile', get_current_profile(request).profile_slug_url)


def get_current_profile(request):
    return Profile.objects.get(profile_user=request.user)


def get_profile_by_id(profId):
    return Profile.objects.get(id=int(profId))


def create_follow(request, follow_id):
    profile = get_current_profile(request)
    follow_profile = get_profile_by_id(follow_id)
    if not profile.follower.all():
        FollowModel.objects.create(Follower=profile, Follow=follow_profile)
    else:
        follow = FollowModel.objects.filter(Follower=profile, Follow=follow_profile)
        if follow:
            follow.delete()
        else:
            FollowModel.objects.create(Follower=profile, Follow=follow_profile)


def get_detailview_instance_slug(self):
    slug = self.kwargs.get(self.slug_url_kwarg)
    return slug

def update_profile(request):
    delete_avatar = request.POST.get('delete_avatar')
    delete_profile_bg = request.POST.get('delete_profile_bg')
    
    avatar = request.FILES.get('profile_avatar')
    descr = request.POST.get('profile_description')
    bg = request.FILES.get('profile_bg')
    activity  = request.POST.get('profile_activity')
    profile = Profile.objects.get(profile_user=request.user)
    if avatar:
        profile.profile_avatar = avatar
    elif delete_avatar:
        profile.profile_avatar = None        
    if bg:
        profile.profile_bg = bg
    elif delete_profile_bg:
        profile.profile_bg = bg
    profile.profile_activity = activity
    profile.profile_description = descr
    profile.save()
    
    
def create_folder(request):
    name = request.POST.get('folder_name')
    bg = request.FILES.get('folder_bg')
    
    Folder.objects.create(folder_profile=get_current_profile(request), folder_name=name, folder_bg=bg)
    
    
def update_folder(request):
    name = request.POST.get('folder_name')
    bg = request.FILES.get('folder_bg')
    folder_id = request.POST.get('folder_id')
    delete_bg = request.POST.get('delete_folder_bg')
    
    folder = Folder.objects.get(id=int(folder_id))
    
    folder.folder_name = name
    if bg:
        folder.folder_bg = bg        
    elif delete_bg:        
        folder.folder_bg = None
    # else:
    #     folder.folder_bg = bg
        
    folder.save()
    