from django import forms
from .models import Product,Category,Vendor
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class AutheticationUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CreateVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"