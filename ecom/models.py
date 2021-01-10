from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_desc = models.TextField(max_length=500)


class Product(models.Model):
    name = models.CharField(max_length=90)
    product_image = models.ImageField(upload_to='product_image')
    price = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField()
