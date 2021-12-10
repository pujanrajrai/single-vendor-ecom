from django.urls import path
from . import views

app_name = 'ecom'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('addtocart/<slug:slug>', views.addtocart, name='add_to_cart'),
    path('cart/', views.viewcart, name='cart'),
    path('deletecart/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search_product, name='search')

]
