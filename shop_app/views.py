from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("Home Page")
