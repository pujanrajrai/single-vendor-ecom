from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_desc = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(max_length=255)
    product_image = models.ImageField(upload_to='product_image')
    price = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField()

    def product_category(self):
        return self.category.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name+"-"+str(self.id))
        super(Product, self).save(*args, **kwargs)

