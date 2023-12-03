from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Collectable, Genre, Platform
from .forms import CollectableForm


def all_collectables(request):
    """ A view to show all collectables, including sorting and search queries"""

    collectables = Collectable.objects.all()
    query = None
    genres = None
    platforms = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            collectables = collectables.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'platform' in request.GET:
            platforms = request.GET['platform'].split(',')
            collectables = collectables.filter(platform__name__in=platforms)
            platforms = Platform.objects.filter(name__in=platforms)

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
        'current_genres': genres,
        'current_platforms': platforms,
    }

    return render(request, 'collectables/collectables.html', context)


def collectable_detail(request, collectable_id):
    """ A view to show more detail on a single collectable"""

    collectable = get_object_or_404(Collectable, pk=collectable_id)

    context = {
        'collectable': collectable,
    }

    return render(request, 'collectables/collectable_detail.html', context)


def add_collectable(request):
    """Add a collectable to the store"""
    if request.method == 'POST':
        form = CollectableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added collectable!')
            return redirect(reverse('add_collectable'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = CollectableForm()
    
    template = 'collectables/add_collectable.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_collectable(request, collectable_id):
    """Edit a collectable to the store"""
    collectable = get_object_or_404(Collectable, pk=collectable_id)
    if request.method == 'POST':
        form = CollectableForm(request.POST, request.FILES, instance=collectable)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('collectable_detail', args=[collectable.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = CollectableForm(instance=collectable) 
        messages.info(request, f'You are editing {collectable.name}')

    template = 'collectables/edit_collectable.html'
    context = {
        'form': form,
        'collectable': collectable,
    }

    return render(request, template, context)

