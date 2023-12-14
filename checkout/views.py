from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'strip_public_key': 'pk_test_51ONMorKLenxX6idK0UxaLWzRaxcFfsX2Wl9lVb3qyvXxLSh7v5HGyCW6RYp2g5a9eHFs86qYjMEEV1Q4PC3cA6m600BjGsEDXe',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)