from django.shortcuts import render
from .models import Product,Category


# Create your views here.

def home(request):
    context = {"products": Product.objects.all()}
    return render(request, 'ecom/home.html', context)
