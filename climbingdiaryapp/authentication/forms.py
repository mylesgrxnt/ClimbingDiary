# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
  username = forms.CharField(max_length=63)
  password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class UserSignUpForm(UserCreationForm):
  username = forms.CharField(max_length=63)
  name = forms.CharField(max_length=63)
  email = forms.EmailField()
  password1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
  password2 = forms.CharField(max_length=63, widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
