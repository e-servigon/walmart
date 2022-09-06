from django.shortcuts import render
from .forms import * 
from .models import *
from django.contrib.auth import authenticate, login 
# Create your views here.

def loginuser(request):
    login_form = AutheticationUserForm()
    contexto = {'login_form': login_form}
    return render(request,'login.html',contexto)

def createuser (request):

    return render(request,'createuser.html',{})

def home (request):
    return render(request,'home.html',{})

def vendor(request):
    return render(request,'vendor.html',{})

def category(request):
    return render(request,'category.html',{})

def product(request):
    return render(request,'product.html',{})

def logoutuser(request):
    print("salida")