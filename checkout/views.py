from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('collectables'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OGrHuDBXYpHsepji2KU5QBdWGHaiPtssx2aTzgO1l0YNrocVLHn4KNLTK9V4rqRReD7l3TCwLVChNX4b7TjjOPV00VfyQbVkO',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
