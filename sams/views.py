from itertools import count
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import * 
from .models import *
from django.utils import timezone

def createuser (request):
    user_form = CreateUserForm()
    user_profile = UserProfileForm()
    contexto = {'user_form': user_form}
    contexto['user_profile_form']=user_profile
    if request.method== 'POST':
        print(request.POST)
        user_form = CreateUserForm(request.POST)
        user_profile=UserProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user_to_profile = User.objects.get(username=request.POST.get('username'))
            user_extended_data = ExtendedData.objects.create(user=user_to_profile,user_type=request.POST.get('user_type'))
            user_extended_data.save()
            return redirect('login')
    return render(request,'createuser.html',contexto)

@login_required
def home (request):
    user_request = User.objects.get(username=request.user.username)
    user_extended_data = ExtendedData.objects.get(user=user_request)
    contexto = {'user_data': user_request,'user_extended_data':user_extended_data}
    print(user_request.username)
    return render(request,'home.html',contexto)

@login_required
def vendor(request):
    vendor_list = Vendor.objects.all()
    count = Vendor.objects.count()
    data_context = {'vendor_list':vendor_list}
    vendor_form = CreateVendorForm()
    data_context['vendor_form'] = vendor_form

    if count == 0 :
        data_context['empty_vendor'] = True
    
    if request.method == 'POST':
        print("entre en post")
        vendor_form = CreateVendorForm(request.POST)
        print(vendor_form.errors)
        if vendor_form.is_valid():
            try:
                vendor_validate = Vendor.objects.get(vendor_name=request.POST.get('vendor_name'))
                if vendor_validate is not None:
                    data_context['vendor_exist'] = True
                    print("imprimir vendor")
                    print(vendor_validate)
            except:
                print("en catch")
                vendor_form.save()
                return redirect('vendor')
        
    return render(request,'vendor.html',data_context)

@login_required
def category(request):
    return render(request,'category.html',{})

@login_required
def product(request):
    product_list = Product.objects.filter(deleted_date__isnull=True)
    product_form = CreateProductForm()
    count = Product.objects.count()
    data_context = {'product_form': product_form}
    data_context['product_list']= product_list

    if count == 0 :
        data_context['empty_product'] = True
    
    if request.method == 'POST':
        product_form = CreateProductForm(request.POST)
        if product_form.is_valid():
            try:
                product_validate = Product.objects.get(product_sku=request.POST.get('product_sku'))
                print (product_validate)
                if product_validate is not None:
                    data_context['product_exist'] = True
            except:
                print(product_form.fields.values)
                product_form.save()
                return redirect('product')
        print(product_form.errors)
        
    return render(request,'product.html',data_context)
    
@login_required
def delete_product (request, product_id):
    product = Product.objects.get(pk=product_id)
    data_context = {'product':product}
    if request.method == 'POST':
        print (request.POST)
        if 'yes' in request.POST:
            product.deleted_date = timezone.now()
            product.save()
            return redirect('product')
        elif 'no' in request.POST:
            return redirect('product')
    return render(request,'delete_product.html',data_context)

@login_required
def search_product (request):
    productsearch_form = SearchProductForm() 
    data_context = {'productsearch_form': productsearch_form}
    data_context['empty_search'] = True
    if request.method == 'POST':
        productsearch_form = SearchProductForm(request.POST) 
        if productsearch_form.is_valid():
            product_list = Product.objects.filter(product_name__contains=request.POST.get('product_name')).filter(deleted_date__isnull=True)
            data_context['product_list'] = product_list
            data_context['empty_search'] = False
    
    return render(request,'search_product.html',data_context)