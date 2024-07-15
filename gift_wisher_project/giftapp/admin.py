from django.contrib import admin
from .models import FriendGroups,Membership,UserProfile,Gift
# Register your models here.

admin.site.register(FriendGroups)
admin.site.register(UserProfile)
admin.site.register(Gift)
admin.site.register(Membership)