from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from artworks.models import Artwork


def cart_contents(request):

    cart_items = []
    total = 0
    artwork_count = 0
    cart = request.session.get('cart', {})
    frame_price = 0

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            artwork = get_object_or_404(Artwork, pk=item_id)
            frame_price = artwork.price * Decimal(settings.FRAME_PERCENTAGE)
            total += item_data * artwork.price + frame_price
            artwork_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'artwork': artwork,
                'frame_price': frame_price,
            })
        else:
            artwork = get_object_or_404(Artwork, pk=item_id)
            for frame, item_data in item_data['items_by_frame'].items():
                total += item_data * artwork.price + frame_price
                artwork_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'artwork': artwork,
                    'frame_price': frame_price,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'artwork_count': artwork_count,
        'frame_price': frame_price,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        # 'frame_price': settings.FRAME_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
