from django.shortcuts import render
from fatora.models import Products,Orders,Customer_user
# Create your views here.
from django.shortcuts import render, redirect
from .models import CartItem
from django.core.mail import send_mail
from .tasks import mail
from django.contrib import messages
def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    if request.method == "POST":
        product = Products.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    
    
    
        quantity = request.POST.get("quantity")
        cart_item.quantity = quantity
        cart_item.save()
        cart_items = CartItem.objects.filter(user=request.user)
        
        total_price = sum(item.product.price * item.quantity for item in cart_items)





        context={
            "products":product,
            "totle":total_price
        }

        return render(request,'one_prodact.html',context=context)
    
    prices = CartItem.objects.filter(user=request.user).values_list('product__price', flat=True)
    totle=sum(prices)
    product = Products.objects.get(id=product_id)
    cart_items = CartItem.objects.filter(user=request.user)
        
    total_price = sum(item.product.price * item.quantity for item in cart_items)
        
    context={
            "products":product,
            "totle":total_price
        }


    return render(request,'one_prodact.html',context=context)





def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')


def pay(request):
      


    return render(request,'payment.html')

#from background_task import background
import asyncio


def pay2(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        
        if len(phone) < 11:
            messages.error(request, 'Enter correct number')

        else:
          
          if email is not None and phone is not None:
            
              
            user = Customer_user.objects.get(id=request.user.id)
            print(user.id )
            
            card = CartItem.objects.filter(user=request.user)
            order_items = []
            for item in card:
                 # Create a new Orders instance for each item
                order_items.append(f"{item.product.name} - {item.quantity}")

                producat=Products.objects.get(id=item.product.id)
                print(producat)
                producat.count_order+=1
                producat.save()

            order=Orders()
            order.order = "\n".join(order_items) 
            order.customer = request.user
            order.phone_user = phone
            order.email = email
           

            order.save()
            # Call mail function after the loop
            CartItem.objects.filter(user=request.user).delete()

            
            mail.delay(user.id)

    return render(request, 'payment_2.html')


