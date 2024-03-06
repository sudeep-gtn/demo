from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Sudeep', 'age':19})

def say_goodmorning(request):
    return HttpResponse("Hello I want to say you Good Morning .....")
