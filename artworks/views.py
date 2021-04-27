from django.shortcuts import (
    render, get_object_or_404, redirect, reverse)
from django.contrib import messages
from django.db.models import Q
from .models import Artwork, Category, Artist, Country
from django.db.models.functions import Lower

from .forms import ArtworkForm


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artwork.objects.all()
    query = None
    categories = None
    artists = None
    countries = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                artworks = artworks.annotate(lower_name=Lower('name'))
                artists = artists.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artworks = artworks.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            artworks = artworks.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'artist' in request.GET:
            artists = request.GET['artist'].split(',')
            artworks = artworks.filter(artist__name__in=artists)
            artists = Artist.objects.filter(name__in=artists)

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            artworks = artworks.filter(country__name__in=countries)
            countries = Country.objects.filter(name__in=countries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please enter a search criteria")
                return redirect(reverse('artworks'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            artworks = artworks.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'artworks': artworks,
        'search_term': query,
        'current_sorting': current_sorting,
        'current_categories': categories,
        'current_artists': artists,
        'current_countries': countries,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show artwork details on a new page """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)


def add_artwork(request):
    """ Add an artwork """
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artwork added.')
            return redirect(reverse('add_artwork'))
        else:
            messages.error(
                request, 'Failed to add artwork. \
                    Please check the form or any errors.')
    else:
        form = ArtworkForm()

    template = 'artworks/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_artwork(request, artwork_id):
    """ Edit an artwork """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artwork successfully updated')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(request, 'Failed to update artwork. \
                 Please check the form for any errors.')
    else:
        form = ArtworkForm(instance=artwork)
        messages.info(request, f'You are editing {artwork.name}')

    template = 'artworks/edit_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
        'from_edit': True,
    }

    return render(request, template, context)
