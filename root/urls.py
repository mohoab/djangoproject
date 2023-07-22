from django.urls import path
from root import views




app_name='root'
urlpatterns = [
    path( 'contact',views.contact , name='contact'),
    path( 'aboutus', views.about  , name='about'),
    path( '' , views.homepage , name='home'),
    path( 'trainers' , views.trainers , name='trainers')
]


