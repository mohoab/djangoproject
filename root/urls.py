from django.urls import path
from root import views
urlpatterns = [
    path('hello/',views.say_hello),
    path('about/',views.about),
    path('','homepage')
]

