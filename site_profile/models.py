from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint
from django.urls import reverse


class ProfileID_Manager(models.Manager):
    def create_id(self, profile): #makes random profile id
        id = str(randint(1000,9999))
        if ProfileID.objects.filter(prof_ID=id):
            return ProfileID_Manager.createProfileID()
        else:
            ProfileID.objects.create(profile = profile, prof_ID=id)



class Profile(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_avatar = models.ImageField(upload_to='profile_avatar/', null=True, blank=True)
    profile_bg = models.ImageField(upload_to='profile_bg/', null=True, blank=True)
    profile_description = models.CharField(max_length=100, null=True, blank=True, default='')
    profile_activity = models.CharField(max_length=20, null=True, blank=True)
    profile_slug_url = models.SlugField(max_length=10, default='none')
    
    def __str__(self):
        return self.profile_user.username
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.profile_slug_url})
    
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, *args, **kwargs):
        """On create user model, a profile is automatically created"""
        
        if created and User.username != 'root':
            Profile.objects.create(profile_user = instance)
            ProfileID.objects.create_id(instance.profile)
            instance.profile.profile_slug_url = ProfileID.objects.get(profile = instance.profile).prof_ID
            instance.profile.save()
            
            
class ProfileID(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='profile_id')
    prof_ID = models.SlugField(max_length=10)
    objects = ProfileID_Manager()
    
    def __str__(self):
        return self.prof_ID
    
    
class FollowModel(models.Model):
    Follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
    Follow = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follow')
    
    def __str__(self):
        return f'{self.Follower}-{self.Follow}'
    
class Folder(models.Model):
    folder_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='folderProfile', null=True)
    folder_name = models.CharField(max_length=100)
    folder_bg = models.ImageField(upload_to="folder_bg/", null=True, blank=True)
    folder_url = models.SlugField(max_length=100, default='folder_u')
    
    def __str__(self):
        return self.folder_name
    
    def get_absolute_url(self):
        return reverse("folder_update", kwargs={"slug": self.folder_url})
    
    
    def save(self, *args, **kwargs):
        """Create folder url"""
        super().save()
        self.folder_url = f'{self.folder_name}-{self.id}'
        super().save()