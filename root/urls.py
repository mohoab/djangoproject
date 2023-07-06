from django.urls import path
from .views import say_hello , about

urlspattern = [
    path('', about),
    path('hello/' , say_hello) ,
]