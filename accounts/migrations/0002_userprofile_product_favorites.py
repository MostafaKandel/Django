# Generated by Django 3.2.12 on 2022-03-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
