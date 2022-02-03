from cart.cart import Cart
from django.conf import settings
from django.shortcuts import render
from menu.models import Product
from .form import OrderCreateForm
from .models import OrderItem
def order_create(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    print(cart)
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            for product_id, description in cart.items():
                product = Product.objects.get(pk=int(product_id))
                OrderItem.objects.create(order=order,
                                         product=product)
                print(product)
            cart.clear()
            return render(request, 'order_created.html', locals())
    else:
        order_form = OrderCreateForm()
        # cart = cart.values()
        prices = [float(float(item['quantity']) * float(item['price'])) for item in cart.values()]
        total_cost = round(sum(prices), 2)
    return render(request, 'order_process.html', locals())