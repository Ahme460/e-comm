# Generated by Django 5.0.1 on 2024-04-23 21:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fatora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer_user',
            name='count_order',
            field=models.IntegerField(default=0),
        ),
    ]