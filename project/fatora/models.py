from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class Customer_user(AbstractUser):
    count_order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        kwargs['using'] = kwargs.get('using', 'default')
        super().save(*args, **kwargs)

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    about_product = models.TextField()
    photo = models.FileField()
    star=models.IntegerField(default=4)
    count_order=models.IntegerField(default=0)
    


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.star > 5:
            self.star = 5
        return super().save(*args, **kwargs)


        
class Orders(models.Model):
    order=models.TextField()
    customer = models.ForeignKey(Customer_user, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)  # تغيير هنا
    phone_user=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    location=models.TextField()

    def __str__(self):
        return self.customer.username

    

