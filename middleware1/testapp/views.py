from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_view(request):
    print('this line printed by view function while processing request')
    return HttpResponse('<h1>custom middleware Demo </h1>')
def home_page_view(request):
    print(10/0)
    return HttpResponse('<h1>This is from home page view</h1>')