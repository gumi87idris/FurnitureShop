from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'shop.html', context)