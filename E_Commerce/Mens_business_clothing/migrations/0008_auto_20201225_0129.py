# Generated by Django 3.1.2 on 2020-12-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mens_business_clothing', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.ManyToManyField(related_name='kg', to='Mens_business_clothing.Basket', verbose_name='Заказ'),
        ),
    ]
