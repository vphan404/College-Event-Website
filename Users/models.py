from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default

class User(AbstractUser):
  is_admin = models.BooleanField(default=False) 
  is_super_admin = models.BooleanField(default=False) 


