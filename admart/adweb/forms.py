from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter First Name'
    })))

    last_name = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter Last Name'
    })))

    username = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter User name'
    })))
    email = forms.EmailField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@mail.com',
        'type': 'email'
    })))
    password1 = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': '*********'
    })))
    password2 = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': '********'
    })))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']