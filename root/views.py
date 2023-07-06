from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return HttpResponse('hellow django')
def about(request):
    return HttpResponse('about django')