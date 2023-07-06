from django.urls import path
from root import views
urlspattern=[
    path('hello/',views.sayhello)
]