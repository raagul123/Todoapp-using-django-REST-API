from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

from django.contrib.auth.models import PermissionsMixin




class UserProfileManager(BaseUserManager):
    def create_user(self,username,name,password=None):
        if not username:
            raise ValueError('Username is not provided')
        user=self.model(username=username,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,name,password):
        user=self.create_user(username,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

        
class TodoItem(models.Model):
    profile_id=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    todo=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo

class UserProfile(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['name']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.username

