from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Категории
class Categories(models.Model):
    name_category = models.CharField(max_length=255,verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_category

#Подкатегории
class Subcategories(models.Model):
    name_subcategories = models.CharField(max_length=255,verbose_name='Подкатегория')
    name_category = models.ForeignKey(Categories,verbose_name='Категория',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name_subcategories

#Размеры
class Size(models.Model):
    name_size = models.CharField(max_length=255,verbose_name='Название размера')
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name_size
#Цвета
class Color(models.Model):
    name_color = models.CharField(max_length=255,verbose_name='Цвет')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name_color
#Продукт
class Product(models.Model):

    name_product = models.CharField(max_length=255,verbose_name='Название продукта')
    category = models.ForeignKey(Categories, verbose_name='Категория', on_delete=models.CASCADE)
    subcategories = models.ForeignKey(Subcategories, verbose_name='Подкатегория', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Картинка 1')
    image_2 = models.ImageField(verbose_name='Картинка 2')
    image_3 = models.ImageField(verbose_name='Картинка 3')
    image_4 = models.ImageField(verbose_name='Картинка 4')
    size = models.ManyToManyField(Size,verbose_name='Размер')
    description = models.TextField(max_length=3000,verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Стоимость товара')
    сolor = models.ManyToManyField(Color,verbose_name='Цвета товара')        

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name_product

#Корзина
class Basket(models.Model):
    user = models.CharField(max_length=255,verbose_name='Имя пользователя')
    name_product = models.CharField(max_length=255,verbose_name='Название продукта')
    size = models.CharField(max_length=255,verbose_name='Размер')
    description = models.TextField(max_length=3000,verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Стоимость товара')
    сolor = models.CharField(max_length=255,verbose_name='Цвет товара') 
    kol = models.BigIntegerField(verbose_name='Кол-во товара')
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return 'Добавление в корзину пользователя ' + str(self.user) + ' товара ' + str(self.name_product)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    date = models.DateTimeField(auto_now = True,verbose_name='Дата и время заказа')
    adress = models.CharField(max_length=255,verbose_name='Адрес доставки')
    order = models.TextField(max_length=3000, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Добавление заказа'


