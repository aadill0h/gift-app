from django.urls import path
from .views import UserFriendGroupsView,FriendGroup_DetailView,wishlist,register,UserProfileView,Homeview

urlpatterns = [
    path('',Homeview, name='homepage'),
    path('friend_groups/',UserFriendGroupsView.as_view(), name ='friend-group-list'),
    path('friend_groups/<int:pk>/',FriendGroup_DetailView.as_view(), name ='friend-group-detail'),
    path('wishlist/<int:user_id>/',wishlist.as_view(), name ='wishlist'),
    path('register/',register, name='register-user'),
    path('user_profile/<int:pk>/',UserProfileView.as_view(), name ='user-profile-detail'),


]