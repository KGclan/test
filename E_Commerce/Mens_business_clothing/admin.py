from django.contrib import admin
from .models import *

class Admin_product_view(admin.ModelAdmin):
    list_display = ('name_product','category','subcategories','description','id')
    search_fields = ['name_product','category__name_category','subcategories__name_subcategories','description']
    list_filter = ['category__name_category','subcategories__name_subcategories']

class Admin_order_view(admin.ModelAdmin):
    list_display = ('user','date','adress','order')
    search_fields = ['user__username','date','adress','order']
    list_filter = ['user','date']

admin.site.register(Categories) 
admin.site.register(Subcategories)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product,Admin_product_view)
admin.site.register(Basket)
admin.site.register(Order,Admin_order_view)

