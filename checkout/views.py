from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('artworks'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IZGxEF03m6Wt0eAaVpw4vIaany08Kngdf43k4EMVjAfTXAUr8SjRgJiY0zvz6puH203CbIiowv5WzKOvMmDDuDK00l0Mivz1s',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
