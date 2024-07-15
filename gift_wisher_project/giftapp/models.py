
from django.db import models
from django.contrib.auth.models import User
import uuid

class FriendGroups(models.Model):
    name = models.CharField(max_length=100)
    #members = models.ManyToManyField(User, through='Membership', related_name='friend_groups')
    group_code = models.CharField(max_length=8, unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.group_code:
            self.group_code = self.generate_unique_code()
        super(FriendGroups, self).save(*args, **kwargs)

    @staticmethod
    def generate_unique_code():
        return uuid.uuid4().hex[:8]

class Gift(models.Model):
    user = models.ForeignKey(User, related_name='gifts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_code = models.CharField(max_length=8, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    friend_groups = models.ManyToManyField(FriendGroups, through='Membership', related_name='memberships', blank=True)

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        if not self.user_code:
            self.user_code = self.generate_unique_code()
        super(UserProfile, self).save(*args, **kwargs)

    @staticmethod
    def generate_unique_code():
        return uuid.uuid4().hex[:8]

class Membership(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    friend_group = models.ForeignKey(FriendGroups, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'friend_group')  # Ensure unique memberships