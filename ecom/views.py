from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
import requests as req

from .models import Product, Category, Order
from .forms import OrderForm
import uuid


# Create your views here.

def home(request):
    context = {"products": Product.objects.all()}
    return render(request, 'ecom/home.html', context)


def product(request, slug):
    context = {"products": Product.objects.filter(slug=slug)}
    return render(request, 'ecom/product.html', context)


@login_required
def addtocart(request, slug):
    user = request.user
    products = Product.objects.get(slug=slug)
    form_data = {"products": products.id, 'user': user}
    form = OrderForm(form_data)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return HttpResponse("error")


@login_required
def viewcart(request):
    cart_item = Order.objects.filter(user=request.user).filter(is_bought=False)
    total = 0
    for cart in cart_item:
        total = total + int(cart.products.price)
    ids = uuid.uuid1()
    print(ids)
    return render(request, 'ecom/cart.html', {'cart_item': cart_item, 'total': total, 'ids': ids})


@login_required
def remove_from_cart(request, id):
    if request.method == "POST":
        Order.objects.filter(id=id).delete()
        return redirect('/')
    return redirect('/')


def test():
    url = "https://uat.esewa.com.np/epay/main"
    d = {'amt': 100,
         'pdc': 0,
         'psc': 0,
         'txAmt': 0,
         'tAmt': 100,
         'pid': 'ee2c3ca1-696b-4cc5-a6be-2c40d929d453',
         'scd': 'EPAYTEST',
         'su': 'http://merchant.com.np/page/esewa_payment_success?q=su',
         'fu': 'http://merchant.com.np/page/esewa_payment_failed?q=fu'}
    resp = req.post(url, d)


@login_required()
def checkout(request):
    if request.method == 'GET':
        print(request.GET.get('total'))
        Order.objects.filter(user=request.user).update(is_bought=True)
        return redirect('ecom:home')
