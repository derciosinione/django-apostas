from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Credito, Aposta

        
# class UserUpdateForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name'] 
        

# class FormApostar(forms.ModelForm):    
#     class Meta:
#         model = Aposta
#         fields = [] 