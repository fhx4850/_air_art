from atexit import register
from django import template
from site_profile.models import FollowModel, Profile


register = template.Library()

@register.simple_tag
def check_avatar(profile):
    if profile.profile_avatar:
        return profile.profile_avatar.url
    else:
        return '/media/profile_avatar/default_img.png'
    

@register.simple_tag
def is_follow(profile_user, follow_id):
    current_profile = Profile.objects.get(profile_user = profile_user)
    follow = Profile.objects.get(id = int(follow_id))
    if FollowModel.objects.filter(Follower = current_profile, Follow = follow):
        return True
    else:
        return False