from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from newApp.models import Product

def home(request):
    products = Product.objects.all()[:4]  # Get first 4 products for home page
    return render(request, 'index.html', {'products': products})
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponse("Contact")
def services(request):
    return HttpResponse("Services")
