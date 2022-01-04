from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
    Users Profile Info Class - inherits from models.Model
    Model class to add additional info that the default model
    does not have (default: username email password first name and
    last name)
"""
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    #def __init__(self):
    #    self.user = user

    #additional classes
    user_site = models.URLField(blank=True)
    user_img = models.ImageField(upload_to='user_imgs/',blank=True)

    def __str__(self):
        return self.user.username

class DeviceProfileInfo(models.Model):
    uowner = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    ndevice = models.CharField(max_length=128)

    #additional classes
    device_token = models.CharField(max_length=256,blank=True)
    device_site = models.URLField(blank=True)
    device_img=models.ImageField(upload_to='device_imgs',blank=True)
