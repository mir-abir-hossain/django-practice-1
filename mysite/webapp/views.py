from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, this is the webapp index page.")

def home(request):
    return render(request=request, template_name="index.html")

def aboutus(request):
    return render(request=request, template_name="aboutus.html")