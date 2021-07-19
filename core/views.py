from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category

def index(request):
    
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')


# def product(request):
#     return render(request, 'core/product.html')