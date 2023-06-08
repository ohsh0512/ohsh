from django.shortcuts import HttpResponse

def my_home(request):
    return HttpResponse("hello world!")