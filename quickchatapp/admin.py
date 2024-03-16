from django.contrib import admin
from .models import Profile, Friend, ChatMessage, FriendRequest

# class ProfileAdmin(admin.ModelAdmin):
#     list_filter = ['user']
#     list_display = ['user']
#     search_fields = ['user']
#     readonly_fields = ['user']

#     class Meta:
#         model = Profile

# Register your models here.
admin.site.register([Profile, Friend, ChatMessage, FriendRequest])
