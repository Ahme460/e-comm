from django.contrib import admin
from django.urls import path,include
from .views import fatora,register,log,prodact,contact,about,testimonial

urlpatterns = [
    path('',fatora,name='fatora'),
    path('register/',register,name='register'),
    path('log/',log,name='log'),
    path('prodact/',prodact,name='prodacct'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path("testimonial/",testimonial,name='testimonial')
    
]
