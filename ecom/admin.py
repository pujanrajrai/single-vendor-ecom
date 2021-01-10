from django.contrib import admin
from .models import Category, Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'product_category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']
