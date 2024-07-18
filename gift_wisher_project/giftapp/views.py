from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FriendGroups,UserProfile,Gift
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages




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
    
class wishlist(ListView):
    model =Gift
    template_name = 'wishlist.html'
    context_object_name = 'gifts'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user =get_object_or_404(User,id=user_id)
        return Gift.objects.filter(user=user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context
        user_id = self.kwargs['user_id']
        context['user'] = get_object_or_404(User, id=user_id)  # Add the user to the context
        return context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to login{username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'giftapp/register.html', {'form': form})
    
class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'user_profile_view.html'
    context_object_name = 'userprofile'
    
