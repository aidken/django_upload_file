from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(req):
    return HttpResponse('Hi, this is the upload page to be built.')

