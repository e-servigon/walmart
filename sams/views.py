from urllib.request import Request
from django.shortcuts import render, redirect
from .forms import * 
from .models import *
from django.contrib.auth import authenticate, login 
# Create your views here.

def loginuser(request):
    login_form = AutheticationUserForm()
    contexto = {'login_form': login_form}
    if request.method == 'POST':
        login_form = AutheticationUserForm(request.POST)
        user = request.POST.get('username')
        password2 = request.POST.get('password')
        user_authenticate = authenticate(request, username = user, password = password2)
        if user_authenticate is not None:
            login(request, user_authenticate)
            return redirect('home')
    return render(request,'login.html',contexto)

def createuser (request):
    user_form = CreateUserForm()
    contexto = {'user_form': user_form}
    if request.method== 'POST':
        print(request.POST)
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    return render(request,'createuser.html',contexto)

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