
from django.contrib import admin
from .models import Customer_user, Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order', 'get_customer_name', 'date', 'phone_user', 'email')

    def get_customer_name(self, obj):
        return obj.customer.username if obj.customer else ''  # Return customer's username if available, otherwise return an empty string

admin.site.register(Customer_user)
admin.site.register(Orders, OrdersAdmin)
# Register your models here.
from django.contrib import admin
from .models import Products


# قم بتسجيل النموذج وواجهة المدير
admin.site.register(Products)

