from django import forms
from ecom.models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'product_image', 'price', 'stock', 'category', 'description']


class CategoryAdd(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_desc']
