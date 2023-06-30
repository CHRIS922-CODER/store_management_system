from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Issuance)
admin.site.register(ProductName)


class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','is_staff','is_super','is_superuser','position','phone_number')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info',{'fields': ('position','phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin) 