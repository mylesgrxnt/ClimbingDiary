from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(max_length=63, unique=True)
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=63)
  password1 = models.CharField(max_length=63)
  password2 = models.CharField(max_length=63)