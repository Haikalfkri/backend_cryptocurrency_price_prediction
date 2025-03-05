from django.contrib import admin
from .models import Role, CryptoData, CustomUser

# Register your models here.
admin.site.register(Role)
admin.site.register(CryptoData)
admin.site.register(CustomUser)