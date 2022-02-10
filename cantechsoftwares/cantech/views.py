from django.contrib.auth import load_backend
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from job.views import *
# Create your views here.


class Home(View):
    def get(self,request):
        
        return render(request,'home.html')

    def post(self,request):
        if request.method == 'POST':
            f_name = request.POST['name']
            f_phoneno = request.POST['phoneno']
            f_email = request.POST['email']
            f_message = request.POST['message']

            feedback = FeedbackModel.objects.create(f_name=f_name,f_phoneno=f_phoneno,f_email=f_email,f_message=f_message)
        
        return render(request,'home.html')     
      
class ComingSoon(View):
    def get(self,request):
        
        return render(request,'comingsoon.html')

class Services(View):
    def get(self,request):
        
        return render(request,'services.html')

class Contact(View):
    def get(self,request):
        
        return render(request,'contact.html')

class Developer(View):
    def get(self,request):

        if not request.user.is_authenticated:
            return redirect('job/user-login')
        else:
            return render(request,'developers.html')



class FeedbackForm(View):
    def post(self,request):
        print("1")
        if request.method == 'POST':
            print("2")
            f_name = request.POST['name']
            f_phoneno = request.POST['phoneno']
            f_email = request.POST['email']
            f_message = request.POST['message']

            feedback = FeedbackModel.objects.create(f_name=f_name,f_phoneno=f_phoneno,f_email=f_email,f_message=f_message)
        
        return render(request,'home.html') 

class AboutUs(View):
    def get(self,request):
        
        return render(request,'about_us.html')
