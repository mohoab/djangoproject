from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return render(request,'root/contact.html')
def about(request):
    return render(request , 'root/about.html')
def homepage(request):
    hdic = {'name':'ahmad'}
    return render(request ,'root/index.html' , context= hdic)