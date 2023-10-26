from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, get_user_model

# Create your views here.

def login_page(request):
  form = forms.LoginForm()
  message = ''
  if request.method == 'POST':
    print('postmethod')
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data['username'],form.cleaned_data['password'])
      user = authenticate(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
      )
      print(user)
      if user is not None:
        login(request, user)
        return redirect('/admin')
      else:
        message = 'Login failed!'
  return render(request, 'login.html', {'form': form, 'message': message})
  
def userSignUp(request):
  if request.method == 'POST':
    form = forms.UserSignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/admin')
  else:
    form = forms.UserSignUpForm()
  return render(request, 'signup.html', {'form': form})