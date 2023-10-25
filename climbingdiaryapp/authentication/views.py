from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate

# Create your views here.

def login_page(request):
  form = forms.LoginForm()
  message = ''
  if request.method == 'POST':
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data['username'],form.cleaned_data['password'])

      user = authenticate(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
      )

      print(user)
      if user is not None:
        # TODO: add functionality that redirects to proper pages
        # if get_user():
        login(request, user)
        message = "congrats on being a user"
        return render(request, 'login.html', {'form': form, 'message': message})
      else:
        message = 'Login failed!'
        print(form.errors)
  return render(request, 'login.html', {'form': form, 'message': message})
  
def userSignUp(request):
  return render(request, 'login.html')
#   form = forms.UserSignUpForm()
#   message = ''
#   if request.method == 'POST':
#     print(request.POST)
#     form = forms.UserSignUpForm(request.POST)
#     if form.is_valid():
#       message = 'successful signup'
#       user = form.save()
#       # auto-login user
#       login(request, user)
#       return redirect('/watches/', {'form': form, 'message': message})
#     else:
#       print(form.errors)
#       message = "signup failed"
#   return render(request, 'studentSignUp.html', context={'form': form, 'message': message})