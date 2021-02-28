from django.views.generic.detail import SingleObjectMixin

from .models import *

class CategoryMixin(SingleObjectMixin):

    def get_cat(self, **kwargs):    
        category = Categories.objects.all()
        subcategory = Subcategories.objects.order_by("name_category")
        cont = {
            'category_list': category,
            'subcategory_list': subcategory,
        }
        return cont

    def get_prod(self, **kwargs):    
        product = Product.objects.all()
        cont = {
            'product_list' : product,
        }
        return cont
    