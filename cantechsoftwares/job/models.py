from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, blank=True, null=True,) 
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,null=True,blank=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    domain = models.CharField(max_length=100,null=True,blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    total_projects = models.IntegerField(default=0)
    age = models.IntegerField(default=0,null=True,blank=True)
    experience = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.user.username

class RecruiterModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    password = models.CharField(max_length=100)
