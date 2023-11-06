from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Campos comunes a todos los usuarios
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rut = models.CharField(max_length=20)
    email = models.EmailField(unique=True)  # Correo electrónico
    password = models.CharField(max_length=250)
    
    def __str__(self):
        return self.username

class NormalUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class ProviderUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=250)  # Nombre de Fantasía
    legal_name = models.CharField(max_length=250)  # Razón Social
    region = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    commune = models.CharField(max_length=250)
    category_id = models.CharField(max_length=250)
    size_id = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    web_url = models.CharField(max_length=250, blank=True, null=True)  # Sitio web (opcional)
    recaptcha = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username