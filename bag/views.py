from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Collectable


def view_bag(request):
    """ A view that renders the bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a product to the bag"""

    collectable = get_object_or_404(Collectable, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += 1
    else:
        bag[item_id] = 1
        messages.success(request, f'Added {collectable.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    bag = request.session.get('bag', {})

    try:
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
