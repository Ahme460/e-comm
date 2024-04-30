# Generated by Django 5.0.1 on 2024-04-27 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_remove_cartitem_product_cartitem_product'),
        ('fatora', '0004_products_star'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fatora.products'),
            preserve_default=False,
        ),
    ]
