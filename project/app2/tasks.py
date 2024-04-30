from django.core.mail import send_mail
from django.contrib import messages
from fatora.models import Orders,Customer_user

from django.shortcuts import render
from . models import CartItem
import asyncio
from celery import shared_task
@shared_task
def mail(user_id):
    user = Customer_user.objects.get(id=user_id)
    orders = Orders.objects.filter(customer_id=user_id)
    prices = CartItem.objects.filter(user=user).values_list('product__price', flat=True)

    subject = 'Thank You for Choosing Our Montages'
  
  
    message = f'''
    Hi {user.username}, 

    We hope this message finds you well and filled with excitement for your upcoming projects!

    First and foremost, we want to extend our heartfelt gratitude for choosing our montages. Your support means the world to us, and we're truly honored to be a part of your creative journey.

    Our montages are carefully crafted with passion and dedication to help bring your visions to life. Whether you're looking to add a touch of cinematic flair to your videos, create memorable presentations, or tell compelling stories, we're here to provide you with the tools you need to succeed.

    Each montage you've purchased is a testament to your commitment to excellence, and we're thrilled to be by your side every step of the way. Should you ever need assistance or have any questions, please don't hesitate to reach out to us. We're here to support you and ensure that your experience with our montages is nothing short of extraordinary.

    Once again, thank you for choosing us. We can't wait to see the incredible creations you'll bring to life with our montages!

    Warm regards,
    '''

  
    app_email = 'ahmeoon1234@gmail.com'
    print('email is')
 
    # Send mail after the loop
    send_mail(
        subject=subject,
        message=message,
        from_email=app_email,

        recipient_list=[user.email],  # Send to the user's email
        fail_silently=False,
    )