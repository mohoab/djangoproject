from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return render(request,'root/contact.html')
def about(request):
    return render(request ,'root/about.html')
def homepage(request):
    return render(request ,'root/index.html')
def trainers(request):
    return render(request ,'root/trainers.html')
def courses(request):
    return render(request ,'root/courses.html')