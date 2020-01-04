from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#vi created to help urls.py -pages
def index(request):
    return  HttpResponse('<h1>Hello!</h1>')
