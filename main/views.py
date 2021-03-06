import cart.cart as Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product


def index(request):
    return render(request, 'index.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'shop.html', context)

"""Cart views"""


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()       # если нам надо логинится на определенный логин, то пишем login_url=
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')