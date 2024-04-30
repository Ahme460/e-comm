from django.shortcuts import render,redirect
from .models import  Customer_user , Orders, Products
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login


from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        checkbox_value = request.POST.get('checkbox_name', False)

        request.session['email'] = email

        if username and email and password:
            existing_users = Customer_user.objects.filter( Q(email=email))

            if existing_users:
                messages.error(request, 'Email already exists.')
            elif password != password2:
                messages.error(request, 'Passwords do not match.')
            elif checkbox_value != 'on':
                messages.error(request, 'Please check the box.')
            else:
                user = Customer_user(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                return redirect('fatora')
        else:
            messages.error(request, 'Please enter all data.')

    return render(request, 'register.html', {'messages': messages.get_messages(request)})
def log (request):

    if request.method=="POST":
        email=request.POST.get("username")
        password=request.POST.get("password")
        print(email,password)

        user=authenticate(username=email,password=password)
        print(user)


        if user is not None:
            login(request,user)
            request.session['email'] = email

            return redirect('fatora')
        else:

            messages.error(request, 'user not found')

    


    return render(request,'login.html')



def fatora(request):
    products = Products.objects.all()
    las_products=Products.objects.order_by('-created_at')[:3]
    top_three_products = Products.objects.order_by('-count_order')[:3]
    cheap_products = Products.objects.order_by('price')[:3]

    email=request.session.get('email')
    stars = [int(product.star) for product in products]
    stars=stars
    ahmed=len(stars)
    # استخراج قيم الستار من كل منتج
    context = {
        'las_products':las_products,
        'top_three_products':top_three_products,
        'cheap_products':cheap_products,
        'stars': stars ,
         'ahmed':ahmed # قائمة تحتوي على قيم ستار لكل منتج
    }

    return render(request, 'index.html', context=context)





def prodact(request):

    products = Products.objects.all()

    context = {
        'products': products,
        # قائمة تحتوي على قيم ستار لكل منتج
    }

    return render(request,'product.html',context=context)




def contact(request):

    return render(request,'contact.html')




def about(request):

    return render(request,'about.html')




def testimonial(request):

    return render(request,"testimonial.html")