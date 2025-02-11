# from django.shortcuts import render

# Create your views here.
# commented out #from django.shortcuts import render

# added below
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!/Hallo Welt!")
