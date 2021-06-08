from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# model import
from .models import Quser

# Dashboard View
class Dashboard(View):
    def get(self, request,*args,**kwargs):    
        context={

        }
        return render(request,'account/dashboard/dashboard.html', context)

# Register View
class Register(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render (request,'account/user_info/register.html')
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username_check = User.objects.filter(username=username)
        email_check = Quser.objects.filter(email=email)
        if username_check:
            messages.warning(request,'Username Already Exitx!!')
            # Redirect to same Page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif password1 != password2:
            messages.warning(request,'Password didnot Match')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            auth_info ={
                'username':username,
                'password':make_password(password1)
            }
            user = User(**auth_info)
            user.save()
        if email_check:
            messages.warning(request,'Email already Exits !!')
            # redirect to same page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            user_obj = Quser(user=user,email=email, first_name =f_name, last_name =l_name)
            user_obj.save(user_obj)
            messages.success(request,'Please Login to Continue')
            return redirect('login')

# Login View 
class LoginView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return redirect(request,'account/user_info/login.html')




