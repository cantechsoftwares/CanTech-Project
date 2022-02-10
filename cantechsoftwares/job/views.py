from email import message
from django.contrib.auth import authenticate, load_backend, login, logout
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User
from cantech.views import *

# Create your views here.

class Portal(View):
    def get(self,request):
        
        return render(request,'portal.html')

class Admin_login(View):
    def get(self,request):
        
        return render(request,'admin_login.html')

class User_login(View):
    def post(self,request):
        if request.method == 'POST':
            inorup = request.POST['inorup']
            # FOR LOGIN
            if inorup == 'login':
                username = request.POST['uname']
                password = request.POST['psswd']
                user = authenticate(username=username, password=password)
                if user:
                    try:
                        userm = UserModel.objects.get(user=user)
                        if userm.type == 'Applicant':
                            login(request, user)
                            message = "Login Successfull"
                            return redirect('developer')
                    except Exception as e:
                        print(e)
                        messages.error(request, 'Invalid Username or Password')
                        return render(request, 'user_login.html')
                else:
                    message = 'Invalid Username or Password'
                    return render(request, 'user_login.html')
                return redirect('Portal')   
                

            # FOR SIGNUP
            elif inorup == 'signup':
                uname = request.POST['uname']
                uemail = request.POST['uemail']
                uphno = request.POST['uphno']
                psswd = request.POST['psswd']
                type = "Applicant"
                try:
                    user = User.objects.create_user(first_name=uname,username=uemail,password=psswd)
                    UserModel.objects.create(user=user,uname=uname,uemail=uemail,uphone=uphno,password=psswd,type=type)
                    return render(request,'signup.html',{uname:'uname',uemail:'uemail',uphno:'uphno',psswd:'psswd',type:'type'})
                except Exception as e:
                    return render(request,'user_login.html')   
                 
        

    def get(self,request):
        
        return render(request,'user_login.html')

class Recruiter_login(View):
    def get(self,request):
        
        return render(request,'recruiter_login.html')


class Signup(View):
    def get(self,request):
        
        return render(request,'signup.html')

