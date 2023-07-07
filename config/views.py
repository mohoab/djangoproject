from django.http import HttpResponse

def winner(request):
    return HttpResponse('youare winner')
