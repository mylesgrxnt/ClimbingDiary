from django.urls import path
from . import views

urlpatterns = [
    path('register', views.userSignUp, name='register'),
    path('',views.login_page, name = 'login_view')
]
