from .models import Basket,Order
from django.forms import ModelForm
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Basket
        fields = ['user','name_product','size','description','price','сolor','kol']

class ZakazForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user','adress','order']