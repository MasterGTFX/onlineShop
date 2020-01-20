# Generated by Django 3.0 on 2020-01-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_productincart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, to='shop.ProductInCart')),
            ],
        ),
    ]