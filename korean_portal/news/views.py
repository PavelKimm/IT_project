from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>News Homepage</h1>')

def about(request):
    return HttpResponse('<h1>News about page</h1>')
    
