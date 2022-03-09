from django import forms
from .models import Profile
from django.forms import fields, widgets, Textarea, FileInput, TextInput

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_avatar', 'profile_bg', 'profile_description', 'profile_activity')
        
        widgets= {
            'profile_description':Textarea(),
            'profile_avatar': FileInput(attrs={
                'accept': 'image/jpeg, image/png',
                'id': 'profile_avatar',
            }),
        }