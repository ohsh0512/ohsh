from django.shortcuts import HttpResponse, render

def my_home(request):
    return HttpResponse("hello world!")

def index(request):
    return render(request, 'index.html')