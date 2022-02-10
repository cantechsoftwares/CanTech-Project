import email
from django.db import models

# Create your models here.

class FeedbackModel(models.Model):
    f_name = models.CharField(max_length=30,blank=True)
    f_phoneno = models.CharField(max_length=12,blank=True)
    f_email = models.EmailField()
    f_message = models.TextField(max_length=500)

