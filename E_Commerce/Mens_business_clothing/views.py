from django.shortcuts import render,redirect ,HttpResponse
from django.views.generic.base import View
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import OrderForm,ZakazForm

from .models import *
from .mixins import CategoryMixin

class BaseView(CategoryMixin,View):
    def get(self,request):
    #    Поиск !
        def search():
            search_query = request.GET.get('search','')

            if search_query:
                product = Product.objects.filter(Q(name_product__icontains=search_query))
            else:
                product = Product.objects.all()
            cont = {
                'product_list': product,
            }
            return cont
        content = {
        }
        content.update(self.get_cat())
        content.update(search())
        return render(request, 'e_commerse_page/index.html', content)
class ProductDetailView(CategoryMixin,View):
    def get(self,request,slug):
        product = Product.objects.get(slug = slug)
        content = {
            'product_view': product
        }
        content.update(self.get_cat())
        content.update(self.get_prod())
        return render(request,'e_commerse_page/product_detail.html',content)

    def post(self,request,slug):
        product = Product.objects.get(slug = slug)
        error = ''
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                error = 'Вы не верно заполнили форму'

        form = OrderForm(request.POST, request.FILES)
        content={
            'form':form,
            'error':error,
        }
        

class CategoryView(CategoryMixin,View):
    def get(self,request,slug):
        category_view = Categories.objects.get(slug=slug)
        content = {
            'category_views' : category_view,
        }
        content.update(self.get_cat())
        content.update(self.get_prod())
        return render(request,'e_commerse_page/category_detail.html',content)

class SubcategoryView(CategoryMixin,View):
    def get(self,request,slug):
        subcategory_view = Subcategories.objects.get(slug=slug)
        content = {
            'subcategory_views' : subcategory_view,
        }
        content.update(self.get_cat())
        content.update(self.get_prod())
        return render(request,'e_commerse_page/subcategory_detail.html',content)

class ShopBasket(CategoryMixin,View):
    def get(self,request,username):
        username = User.objects.get(username=username)
        product = Basket.objects.filter(user=username)
        sum = product.aggregate(models.Sum('price'))
        content = {
            'user' : username,
            'product_list' : product,
            'sum_list': sum,
        }
        content.update(self.get_cat())
        return render(request,'e_commerse_page/shop_basket.html',content)

class ShopBasketDelete(CategoryMixin,View):
    def get(self,request,id):
        product = Basket.objects.filter(id=id).delete()
        content = {
            'product_list' : product,
        }
        content.update(self.get_cat())
        return redirect('/')

class Order(CategoryMixin,View):
    def get(self,request,username):
        username = User.objects.get(username=username)
        basket = Basket.objects.filter(user=username)
        content = {
            'user' : username,
            'basket_list' : basket,
        }
        content.update(self.get_cat())
        return render(request,'e_commerse_page/order.html',content)

    def post(self,request,username):
        username = User.objects.get(username=username)
        basket = Basket.objects.filter(user=username)
        if request.method == 'POST':
            form = ZakazForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                return HttpResponse(u'Куда прёшь?')

        form = ZakazForm(request.POST)
        content={
            'form':form,
        }
    