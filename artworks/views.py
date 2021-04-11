from django.shortcuts import (
    render, get_object_or_404, redirect, reverse)
from django.contrib import messages
from django.db.models import Q
from .models import Artwork


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artwork.objects.all()
    query = None

    if request.GET:
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
