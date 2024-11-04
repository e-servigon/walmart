from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import * 
import google.generativeai as genai
import json


def model_configuration():
    genai.configure(api_key='poner aqui el api')

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config)
    
    return model

def llm_prompt_engineering(model,vendor_sentiment_result):
    chat = model.start_chat(
        history=[
            {"role": "user", 
            "parts": '''Vas a recibir una frase y me tienes que analizar el sentimiento de la frase, 
            el formato que me vas a responder es de esta manera 
                "{"sentiment": "result"}"
            donde result es el sentimiento y me lo debes de clasifcar en positive, neutral o negative segun sea el caso. El resultado damelo en español.'''
            },
        ]
    )

    response = chat.send_message(vendor_sentiment_result)
    print("el json original es:", response.text)
    return response.text


# Create your views here.
@login_required
def home (request):
    return render(request,'home.html',{})

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
    return render(request,'create_user.html',contexto)

@login_required
def vendor (request):
    vendor_list = Vendor.objects.filter(deleted_date__isnull=True)
    vendor_count= Vendor.objects.count()
    vendor_form = CreateVendorForm()
    data_context = {'vendor_list':vendor_list,'vendor_form':vendor_form}
    print("el conteo de proveedores es: ",vendor_count)
    if vendor_count == 0:
        data_context['empty_vendor'] = True

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        vendor_form = CreateVendorForm(request.POST,request.FILES)
        if vendor_form.is_valid():
            try:
                vendor_validate = Vendor.objects.get(vendor_name=request.POST.get('vendor_name'))
                if vendor_validate is not None:
                    data_context['vendor_exist'] = True
            except:
                vendor_sentiment_result = request.POST.get('sentiment_comments')     
                model = model_configuration()
                sentiment_analyzed = llm_prompt_engineering(model,vendor_sentiment_result)
                print(sentiment_analyzed)
                json_data = json.loads(sentiment_analyzed)
                sentiment = json_data["sentiment"]
                print(sentiment)
                vendor_form.sentiment_result = sentiment
                vendor_form.save()
                vendor_to_upd = Vendor.objects.get(vendor_name=request.POST.get('vendor_name'))
                vendor_to_upd.sentiment_result = sentiment
                vendor_to_upd.save()
                return redirect('vendor')

    return render(request,'vendor.html',data_context)

@login_required
def update_vendor (request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    edit_vendor_form = EditVendorForm()
    data_context = {'vendor':vendor,'edit_vendor_form':edit_vendor_form}
    print(vendor)
    
    if request.method == "POST":
        print(request.POST)
        formulario = EditVendorForm(request.POST, instance = vendor)
        if formulario.is_valid():
            formulario.save()
            return redirect('vendor')

    return render(request,'update_vendor.html',data_context)

@login_required
def delete_vendor (request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    data_context = {'vendor':vendor}
    if request.method == "POST":
        print (request.POST)
        if 'yes' in request.POST:
            vendor.deleted_date = timezone.now()
            vendor.save()
            return redirect('vendor')
        elif 'no' in request.POST:
            return redirect('vendor')
    return render(request,'delete_vendor.html',data_context)
