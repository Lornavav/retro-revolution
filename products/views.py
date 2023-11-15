from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Collectable


def all_collectables(request):
    """ A view to show all collectables, including sorting and search queries"""

    collectables = Collectable.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('collectables'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            collectables = collectables.filter(queries)

    context = {
        'collectables': collectables,
        'search_term': query,
    }

    return render(request, 'collectables/collectables.html', context)


def collectable_detail(request, collectable_id):
    """ A view to show more detail on a single collectable"""

    collectable = get_object_or_404(Collectable, pk=collectable_id)

    context = {
        'collectable': collectable,
    }

    return render(request, 'collectables/collectable_detail.html', context)
