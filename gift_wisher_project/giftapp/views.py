from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FriendGroups,UserProfile

class UserFriendGroupsView(LoginRequiredMixin, ListView):
    model = FriendGroups
    template_name = 'user_friend_groups.html'
    context_object_name = 'friend_groups'

    def get_queryset(self):
        user_profile = self.request.user.profile
        return user_profile.friend_groups.all()

class FriendGroup_DetailView(LoginRequiredMixin, DetailView):
    model = FriendGroups
    template_name='friend_groups_desc.html'
    context_object_name='friend_group_desc'
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         friend_group = self.get_object()
         members = UserProfile.objects.filter(membership__friend_group=friend_group,membership__is_member=True)
         #filters UserProfile objects that are associated with the friend_group through the Membership model where is_member is True.
         context['members'] = members
         return context
    


