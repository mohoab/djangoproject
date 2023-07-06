from django.http import HttpResponse

def winner(request):
    return HttpResponse('youare winner')
def hello(request):
    return HttpResponse('hello user')