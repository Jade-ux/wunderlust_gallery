from django.shortcuts import (
    render, get_object_or_404, redirect, reverse)
from django.contrib import messages
from django.db.models import Q
from .models import Artwork, Category, Artist, Country


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artwork.objects.all()
    query = None
    categories = None
    artists = None
    countries = None

    if request.GET:
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

    context = {
        'artworks': artworks,
        'search_term': query,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show artwork details on a new page """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)
