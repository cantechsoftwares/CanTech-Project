from calendar import c
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

class Logout(View): 
    def get(self,request):
        logout(request)
        return redirect('/')
        


class Admin_login(View):
    def post(self,request):
        if request.method == 'POST':
            sername = request.POST['uname']
            password = request.POST['psswd']
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
                        print(userm.type)
                        if userm.user_type == 'Applicant':
                            login(request, user)
                            print('SUCCSESS')
                            message = "Login Successfull"
                            return redirect('developer')
                    except Exception as e:
                        print(e)
                        messages.error(request, 'Invalid Username or Password')
                        return render(request, 'user_login.html',e)
                else:
                    message = 'Invalid Username or Password'
                    return render(request, 'user_login.html',{'message':message})
                return redirect('Portal')   

            # FOR SIGNUP
            elif inorup == 'signup':
                uname = request.POST['uname']
                uemail = request.POST['uemail']
                uphno = request.POST['uphno']
                psswd = request.POST['psswd']
                cpsswd = request.POST['cpsswd']
                type = "Applicant"
                data = {'uname':uname,'uemail':uemail,'uphno':uphno,'psswd':psswd,'type':type}
                print(data)
                if psswd == cpsswd:
                    try:
                        user = User.objects.create_user(first_name=uname,username=uemail,password=psswd,email=uemail)
                        UserModel.objects.create(user=user,uname=uname,uemail=uemail,uphone=uphno,password=psswd,user_type=type)
                        return render(request,'signup.html',{'data':data})
                    except Exception as e:
                        message = 'User Already Exist by this Email or Mobile'
                        return render(request,'user_login.html',{'message':message}) 
                else: 
                    return render(request,'user_login.html',{'message':'Password and Confirm Password does not match'})   

                 
        

    def get(self,request):
        log_type = 'User'
        return render(request,'user_login.html',{'log_type':log_type})

class Recruiter_login(View):
    def post(self,request):
        if request.method == 'POST':
            inorup = request.POST['inorup']
            # FOR LOGIN
            if inorup == 'login':
                username = request.POST['rname']
                password = request.POST['psswd']
                user = authenticate(username=username, password=password)
                if user:
                    try:
                        userm = RecruiterModel.objects.get(user=user)
                        if userm.user_type == 'Recruiter':
                            login(request, user)
                            print('SUCCSESS')
                            message = "Login Successfull"
                            return redirect('recruiter')
                    except Exception as e:
                        print(e)
                        messages.error(request, 'Invalid Username or Password')
                        return render(request, 'recruiter_login.html',e)
                else:
                    message = 'Invalid Username or Password'
                    return render(request, 'recruiter_login.html',{'message':message})
                return redirect('Portal')   

            # FOR SIGNUP
            elif inorup == 'signup':
                rname = request.POST['rname']
                remail = request.POST['remail']
                rphno = request.POST['rphno']
                psswd = request.POST['psswd']
                cpsswd = request.POST['cpsswd']
                company = request.POST['company']
                type = "Recruiter"
                data = {'uname':rname,'uemail':remail,'uphno':rphno,'psswd':psswd,'type':type}
                print(data)
                if psswd == cpsswd:
                    try:
                        user = User.objects.create_user(first_name=rname,username=remail,password=psswd,email=remail)
                        RecruiterModel.objects.create(user=user,rname=rname,remail=remail,rphone=rphno,password=psswd,user_type=type,company=company)
                        # return render(request,'signup.html',{'data':data})
                        return redirect('recruiter')
                    except Exception as e:
                        message = 'User Already Exist by this Email or Mobile'
                        return render(request,'recruiter_login.html',{'message':message}) 
                else: 
                    return render(request,'recruiter_login.html',{'message':'Password and Confirm Password does not match'})   

    def get(self,request):
        log_type = 'Recruiter'
        return render(request,'recruiter_login.html',{'log_type':log_type})


class Signup(View):
    def post(self,request):
        if request.method == 'POST':
            try:
                uemail = request.POST.get('uemail')
                uname = request.POST.get('uname')
                uphno = request.POST.get('uphno')
                domain = request.POST.get('domain')
                user_type = request.POST.get('user_type')
                age = request.POST.get('age')
                experience = request.POST.get('experience')
                resume = request.FILES.get('resume')
                image = request.FILES.get('image')
                city = request.POST.get('city')
                aboutu = request.POST.get('aboutu')
                freelance = request.POST.get('freelance')
                if freelance == 'on':
                    freelance = 1
                else:
                    freelance = 0    

            
                userm = UserModel.objects.filter(uemail=uemail)
                for um in userm:
                    um.uname = uname
                    um.uphone = uphno
                    um.type = user_type
                    um.age = age
                    um.domain = domain
                    um.experience = experience
                    um.resume = resume
                    um.image = image
                    um.city = city
                    um.aboutu = aboutu
                    um.freelance = freelance
                    um.user_type = 'APPLICANT'
                    um.save()


                data = {'uemail':uemail,'uname':uname,'uphno':uphno,'user_type':user_type,'age':age,'experience':experience,'city':city,'aboutu':aboutu}
                
                password = UserModel.objects.get(uemail=uemail).password
                user = authenticate(username=uemail, password=password)
                login(request, user)
                return redirect('developer')
            except Exception as e:
                print(e)
                return render(request,'signup.html',{'message':e})    

    def get(self,request):
        
        return render(request,'signup.html')

