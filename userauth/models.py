from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=50, default="full name")
    location = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='profile_pics', max_length=None, default='null.jpg')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    def __str__(self):
        return self.username
    