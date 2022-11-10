from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Just dummy text
    # return HttpResponse("Hello, world. You're at the polls index.")
    
    # Page from the theme 
    # return render(request, 'pages/dashboard.html')

    # Custom Page  
    return render(request, 'custom.html')

