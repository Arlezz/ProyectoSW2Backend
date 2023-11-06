from django.contrib import admin
from .models import CustomUser, ProviderUser, NormalUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

class ProviderUserAdmin(admin.ModelAdmin):
    model = ProviderUser

class NormalUserAdmin(admin.ModelAdmin):
    model = NormalUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProviderUser, ProviderUserAdmin)
admin.site.register(NormalUser, NormalUserAdmin)

