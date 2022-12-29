from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nombre = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=255)
    direccion = models.CharField(max_length=90)
    telefono = models.IntegerField()
    fnacimiento = models.CharField(max_length=90)
    
    first_name = None
    last_name = None
    username = None
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = []
    
