from django.shortcuts import render
from courses import  models



def courses(request):
    course= models.courses.objects.all()
    context = {
        'courses' : course 
    }
    return render(request ,'courses/courses.html' , context = context)
