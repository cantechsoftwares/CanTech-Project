import email
from inspect import stack
from django.db import models

# Create your models here.

class FeedbackModel(models.Model):
    f_name = models.CharField(max_length=30,blank=True)
    f_phoneno = models.CharField(max_length=12,blank=True)
    f_email = models.EmailField()
    f_message = models.TextField(max_length=500)

class QuotationModel(models.Model):
    qname = models.CharField(max_length=30,blank=True)
    qphone = models.CharField(max_length=12,blank=True)
    qemail = models.EmailField(blank=True)
    qbussiness = models.CharField(max_length=30,blank=True)
    totalpage = models.IntegerField(blank=True)
    stack = models.CharField(max_length=30,blank=True)
    qbudget = models.IntegerField(blank=True)   
    qteam  = models.BooleanField(blank=True)
    qtype = models.CharField(max_length=30,blank=True)