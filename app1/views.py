from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from app1.forms import SignupForm,UpdateUserProfile,UpdateAdminProfile
from django.contrib import messages
from django.contrib.auth.forms import (
                    AuthenticationForm,
                    PasswordChangeForm,
                    SetPasswordForm
                    )
from django.contrib.auth import (
                authenticate,
                login,
                logout,
                get_user,
                update_session_auth_hash
                )
from django.contrib.auth.models import User

# Create your views here.form 


def userinfo(request,id):
    if request.user.is_authenticated:
            if request.user.is_superuser == True:
                user = User.objects.get(pk=id)
                form = UpdateUserProfile(instance=user)
                context = {'form':form,'name':request.user.username}
                return render(request,'app1/userinfo.html',context)
            else:
                return HttpResponse("<h1>You can not see others profile</h1>")
    else:
        return HttpResponseRedirect('/app1/login')

def changepwd2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password Changed successfully!!')
                return HttpResponseRedirect('/app1/profile')
        else:
            form = SetPasswordForm(user=request.user)
        context = {'form':form,'name':request.user.username}
        return render(request,'app1/changepwd2.html',context)
    else:
        return HttpResponseRedirect('/app1/login')

def changepwd1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password Changed successfully!!')
                return HttpResponseRedirect('/app1/profile')
        else:
            form = PasswordChangeForm(user=request.user)
        context = {'form':form,'name':request.user.username}
        return render(request,'app1/changepwd1.html',context)
    else:
        return HttpResponseRedirect('/app1/login')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/app1/login')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                form = UpdateAdminProfile(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                form = UpdateUserProfile(request.POST,instance=request.user)
                users = None
            if form.is_valid():
                form.save()
                messages.success(request,'User Profile Updated')
        else:
            if request.user.is_superuser == True:
                form = UpdateAdminProfile(instance=request.user)
                users = User.objects.all()
            else:
                form = UpdateUserProfile(instance=request.user)
                users = None
        context = {'form':form,
                   'msg':'this is profile page',
                   'name':request.user.username,
                   'users':users}
        return render(request,'app1/profile.html',context)
    else:
        return HttpResponseRedirect('/app1/login')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Done !!')
                    return HttpResponseRedirect('/app1/profile')
        else:
            form = AuthenticationForm()
        context = {'form':form,'name':request.user.username}
        return render(request,'app1/login.html',context)
    else:
        return HttpResponseRedirect('/app1/profile')

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignupForm()
            messages.success(request,'Account Created successfully!!')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request,'app1/signup.html',context)

def index(request):
    context = {'msg':'This is Index Page','name':request.user.username}
    return render(request,'app1/index.html',context)


def app1(request):
    context = {'msg':'This is APP1 Page'}
    return render(request,'app1/index.html',context)
