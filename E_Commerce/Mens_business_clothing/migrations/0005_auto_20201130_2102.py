# Generated by Django 3.1.2 on 2020-11-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mens_business_clothing', '0004_auto_20201126_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='description',
            field=models.TextField(max_length=3000, verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='kol',
            field=models.BigIntegerField(verbose_name='Кол-во товара'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='name_product',
            field=models.CharField(max_length=255, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Стоимость товара'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='size',
            field=models.CharField(max_length=255, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.CharField(max_length=255, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='сolor',
            field=models.CharField(max_length=255, verbose_name='Цвет товара'),
        ),
    ]
