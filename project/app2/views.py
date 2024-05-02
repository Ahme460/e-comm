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
    if request.method == "GET":
        return render(request,'payment.html')
    else:
        import requests as re
        #your api 
        api="ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2T1RjME16QXhMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuR2duRjJjU0pnRThsbVpqRnVGMWdPTHlzaFdlSnpSOVBJTDFkT1RBQ3B0Z3JqckxnUmo5WU43MHZqOGlGYUdVQzZmUm5mQ2tQWDZUbHBkcUVFX3J6NUE="
        #now we send request to get first token
        token = re.post(
            url="https://accept.paymob.com/api/auth/tokens",
            json= {
            "api_key": api
            }
        )
        #get token from resposne
        api_token = token.json().get("token", None)



        #now collect data require from doc that based on type payment
        paylod = {
            "auth_token":  api_token,
            "delivery_needed": "false",
            "amount_cents": "100",
            "currency": "EGP",
            "items": [
                {
                    "name": "ASC1515",
                    "amount_cents": "500000",
                    "description": "Smart Watch",
                    "quantity": "1"
                },
                { 
                    "name": "ERT6565",
                    "amount_cents": "200000",
                    "description": "Power Bank",
                    "quantity": "1"
                }
                ],
            "shipping_data": {
                
            },
                "shipping_details": {
                    
                }
            }
        #send req
        response = re.post(
            url="https://accept.paymob.com/api/ecommerce/orders",
            json=paylod  #data
        )

        #get id form response
        id=response.json().get('id', None)
        

        #now write data payment
        paylod = {
            "auth_token": api_token, # first token 
            "amount_cents": "100", 
            "expiration": 3600, 
            "order_id": f"{id}", # id that i get it form response 
            "billing_data": {
                "apartment": "803", 
                "email": "test@gmail.com", 
                "floor": "42", 
                "first_name": "Clifford", 
                "street": "Ethan Land", 
                "building": "8028", 
                "phone_number": "+201064160586", 
                "shipping_method": "PKG", 
                "postal_code": "01898", 
                "city": "cairo", 
                "country": "EG", 
                "last_name": "Nicolas", 
                "state": "Utah"
            }, 
            "currency": "EGP", 
            "integration_id": 4569633 # this get it from account paymob when add type payment

            }
        #send requests
        response = re.post(
            url="https://accept.paymob.com/api/acceptance/payment_keys",
            json=paylod
        )

        token = response.json().get('token', None)
        #get token
        # print(token, "--------")

        #now open doc and you choice type pay on based on write this payload 
        paylod = {
            "source": {
                "identifier": "01010101010", 
                "subtype": "WALLET"
            },
            "payment_token": token
            }
        response = re.post(
            url="https://accept.paymob.com/api/acceptance/payments/pay",
            json=paylod

        )
        #now get link redirect
        link=response.json().get('redirect_url',None)
        
        return redirect(link)

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


