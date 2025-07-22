from  django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.models import Account
from django.forms.widgets import PasswordInput, TextInput


# Registering an account(ModelForm)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required.Add a valid email adress')
    class Meta:
        model= Account
        fields = ("email", "username", "password1", "password2")


# Authenticating an account(ModelForm)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())





