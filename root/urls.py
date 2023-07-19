from django.urls import path
from root import views
urlpatterns = [
    path('contact/',views.contact),
    path('about/', views.about ),
    path('' , views.homepage)
]

