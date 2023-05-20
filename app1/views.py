from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'msg':'This is Index Page'}
    return render(request,'app1/index.html',context)


def app1(request):
    context = {'msg':'This is APP1 Page'}
    return render(request,'app1/index.html',context)
