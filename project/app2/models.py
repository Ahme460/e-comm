from django.db import models
from fatora.models import Customer_user,Products



# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey( Products ,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Customer_user, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'