from itertools import count
from urllib.request import Request
from django.shortcuts import render, redirect
from .forms import * 
from .models import *
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 

''''def loginuser(request):
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
    return render(request,'login.html',contexto)'''

@login_required
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

@login_required
def home (request):
    return render(request,'home.html',{})

@login_required
def vendor(request):
    vendor_list= Vendor.objects.all()
    contexto = {'vendor_list':vendor_list}
    vendor_form = CreateVendorForm()
    contexto['vendor_form'] = vendor_form
    count= Vendor.objects.count()

    if count== 0:
        print("no hay datos")
        contexto['empty_vendor']= True
    
    if request.method == 'POST':
        print("entre en post")
        vendor_form = CreateVendorForm(request.POST)
        print(vendor_form.errors)
        if vendor_form.is_valid():
            try:
                vendor_validate = Vendor.objects.get(vendor_name=request.POST.get('vendor_name'))
                if vendor_validate is not None:
                    contexto['duplicated_vendor'] = True
                    print("imprimir vendor")
                    print(vendor_validate)
            except:
                print("en catch")
                vendor_form.save()
                return redirect('vendor')
    return render(request,'vendor.html',contexto)

@login_required
def category(request):
    return render(request,'category.html',{})

@login_required
def product(request):
    return render(request,'product.html',{})


