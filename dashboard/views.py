from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, RedirectView

from ecom.models import Product, Order, Category
from accounts.models import MyUser
from .forms import ProductForm


# Create your views here.
@method_decorator([staff_member_required, ], name='dispatch')
class Home(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        cart_item = Order.objects.filter(is_bought=True)
        total = 0
        for cart in cart_item:
            total = total + int(cart.products.price)
        total_user = MyUser.objects.all()
        no_user = total_user.count()
        product = Product.objects.all()
        total_product = product.count()
        context = {"total": total, "no_user": no_user, "total_product": total_product}
        return context


@method_decorator([staff_member_required, ], name='dispatch')
class ShowProduct(TemplateView):
    template_name = 'dashboard/showproduct.html'

    def get_context_data(self, **kwargs):
        product = Product.objects.all()
        context = {'products': product}
        return context


@method_decorator([staff_member_required, ], name='dispatch')
class DeleteProduct(RedirectView):
    url = '/dashboard/showproduct/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        product = Product.objects.get(pk=del_id)
        product.product_image.delete(False)
        Product.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


@method_decorator([staff_member_required, ], name='dispatch')
class AddPhoto(TemplateView):
    template_name = 'dashboard/add.html'

    def get_context_data(self, **kwargs):
        form = ProductForm()
        category = Category.objects.all()
        print(form)
        context = {'category': category,'fm': form}
        return context

    def post(self, request):
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/showproduct/')
        else:
            return HttpResponse('not valid')


@method_decorator([staff_member_required, ], name='dispatch')
class UpdateProduct(View):
    def get(self, request, id):
        pi = Product.objects.get(pk=id)
        category = Category.objects.all()
        return render(request, 'dashboard/updatephoto.html', {'pi': pi, 'category': category})

    def post(self, request, id):
        pi = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dashboard/showproduct')
