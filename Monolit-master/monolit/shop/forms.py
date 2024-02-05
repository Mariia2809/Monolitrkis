from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class RegistrationForm(UserCreationForm):
    model = CustomUser
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'avatar']

        labels = {
            'username': 'Логин',
            'avatar': 'Ава',
            'email': 'Почта'
        }

class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'avatar']