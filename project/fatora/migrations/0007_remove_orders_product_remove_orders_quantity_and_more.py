# Generated by Django 5.0.1 on 2024-04-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fatora', '0006_orders_email_orders_phone_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orders',
            name='order',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
