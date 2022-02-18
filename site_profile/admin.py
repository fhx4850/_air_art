from django.contrib import admin
from . import models


admin.site.register(models.Profile)
admin.site.register(models.ProfileID)
admin.site.register(models.FollowModel)
admin.site.register(models.Folder)