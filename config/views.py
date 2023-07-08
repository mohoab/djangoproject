from django.http import HttpResponse
from django.shortcuts import render
def winner(request):
    wdic={'winner1' : 'alireza' , 'winner2' : 'mohammad' , 'winner3' : 'abbas'}
    return render(request,'config/winner.html' , context = wdic )
