from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def About_me(request):
    return render(request,'desktop-6.html')

def tech_stack(request):
    return render(request,'desktop-4.html')

def projects(request):
    return render(request,'desktop-3.html')

def connect(request):
    return render(request,'desktop-5.html')


