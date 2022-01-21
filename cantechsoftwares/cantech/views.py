from django.contrib.auth import load_backend
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.


class Home(View):
    def get(self,request):
        
        return render(request,'home.html')
      
class ComingSoon(View):
    def get(self,request):
        
        return render(request,'comingsoon.html')
