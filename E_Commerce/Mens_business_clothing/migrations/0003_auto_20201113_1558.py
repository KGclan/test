# Generated by Django 3.1.2 on 2020-11-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mens_business_clothing', '0002_auto_20201103_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(upload_to='', verbose_name='Картинка 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(upload_to='', verbose_name='Картинка 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(upload_to='', verbose_name='Картинка 4'),
        ),
    ]
