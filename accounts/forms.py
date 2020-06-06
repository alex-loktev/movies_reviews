from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    username = forms.CharField(min_length=4, max_length=35, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]+$',
            message='Username isn\'t valid',
            code='invalid_username'
        )
    ])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
