from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('delete/<int:id>',views.DeleteProduct.as_view(),name='delete'),
    path('showproduct/',views.ShowProduct.as_view(),name='show_product'),
    path('addproduct/',views.AddPhoto.as_view(),name='add_product'),
    path('updateproduct/<int:id>',views.UpdateProduct.as_view(),name='update_product'),

]
