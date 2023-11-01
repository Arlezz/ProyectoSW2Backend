from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    communeId = models.CharField(max_length=50)
    businessName = models.CharField(max_length=50)
    categoryId = models.CharField(max_length=50)
    sizeId = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    webUrl = models.CharField(max_length=50)
    recaptcha = models.CharField(max_length=50)