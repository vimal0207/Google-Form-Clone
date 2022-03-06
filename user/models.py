from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.BigIntegerField(blank=True,null=True,unique=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"