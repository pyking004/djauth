from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from app1.forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.form 

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request,'app1/login.html',context)

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
    context = {'msg':'This is Index Page'}
    return render(request,'app1/index.html',context)


def app1(request):
    context = {'msg':'This is APP1 Page'}
    return render(request,'app1/index.html',context)
