from django.contrib import admin
from .models import MyUser
# Register your models here.
@admin.register(MyUser)
class User(admin.ModelAdmin):
    list_display = ['username','email','is_admin','is_active']
