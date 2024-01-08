from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from userauth.models import User

from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'username',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    
    password = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'password',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", 'full_name', 'last_name', 'location', "email", "password1", "password2")
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'Your username',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'Full Name',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    
    location = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'Location',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'Your email',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'Create password',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": 'Confirm your password',
        "class": "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"
    }))
    


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ["new_password1", "new_password2"]


class PasswordResetForm(PasswordResetForm):
        fields = ["email"]