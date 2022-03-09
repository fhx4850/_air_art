from site_profile.models import FollowModel, Profile, Folder
from exceptions.BaseExceptionsMixin import BaseExceptionsMixin
   
    
class ProfileService(BaseExceptionsMixin):
    """This class contains all the logic for the profile."""
    
    # wrongDataReceived = BaseExceptionsMixin.getWrongDataReceived()
    objectDoesNotExist = BaseExceptionsMixin.getObjectDoesNotExist()
    creationError = BaseExceptionsMixin.getCreationError()
    updateError = BaseExceptionsMixin.getUpdateError()

    catchExcept = BaseExceptionsMixin.baseException
    
    
    @catchExcept(objectDoesNotExist, 'Profile not found')
    def get_current_profile(self, request):
        return Profile.objects.get(profile_user=request.user)


    @catchExcept(objectDoesNotExist, 'Profile not found')
    def get_profile_by_id(self, profId):
        Profile.objects.get(id=int(profId)) 
    
    
    @catchExcept(creationError, 'Failed to create follow')
    def create_follow(self, request, follow_id):
        """Create and delete follows"""
        
        profile = self.get_current_profile(request)
        follow_profile = self.get_profile_by_id(follow_id)
        if not profile.follower.all():
            FollowModel.objects.create(Follower=profile, Follow=follow_profile)
        else:
            follow = FollowModel.objects.filter(Follower=profile, Follow=follow_profile)
            if follow:
                follow.delete()
            else:
                FollowModel.objects.create(Follower=profile, Follow=follow_profile)
    
    
    @catchExcept(objectDoesNotExist, 'Profile not found')
    @staticmethod
    def get_detailview_instance_slug(self):
        """Returns a detailView object using slug"""
        
        slug = self.kwargs.get(self.slug_url_kwarg)
        return slug
    
    
    @catchExcept(updateError, 'Error while updating profile')
    def update_profile(self, request):
        """Handling html form to update profile"""
        
        delete_avatar = request.POST.get('delete_avatar')
        delete_profile_bg = request.POST.get('delete_profile_bg')
        
        avatar = request.FILES.get('profile_avatar')
        descr = request.POST.get('profile_description')
        bg = request.FILES.get('profile_bg')
        activity  = request.POST.get('profile_activity')
        profile = Profile.objects.get(profile_user=request.user)
        if avatar and not delete_avatar:
            profile.profile_avatar = avatar
        elif delete_avatar:
            profile.profile_avatar = None        
        if bg and not delete_profile_bg:
            profile.profile_bg = bg
        elif delete_profile_bg:
            profile.profile_bg = None
        profile.profile_activity = activity
        profile.profile_description = descr
        profile.save()
    
    
    @catchExcept(creationError, 'Error while creating folder')
    def create_folder(self, request):
        name = request.POST.get('folder_name')
        bg = request.FILES.get('folder_bg')
        
        Folder.objects.create(folder_profile=self.get_current_profile(request), folder_name=name, folder_bg=bg)
        
    
    @catchExcept(updateError, 'Error while updating folder')
    def update_folder(self, request):
        """Handling html form to update folder"""
        
        name = request.POST.get('folder_name')
        bg = request.FILES.get('folder_bg')
        folder_id = request.POST.get('folder_id')
        delete_bg = request.POST.get('delete_folder_bg')
        
        folder = Folder.objects.get(id=int(folder_id))
        
        folder.folder_name = name
        if bg and not delete_bg:
            folder.folder_bg = bg        
        elif delete_bg:        
            folder.folder_bg = None        
        folder.save()