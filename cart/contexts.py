from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    artwork_count = 0
    # frame_price = None

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    
    # if FRAME_WHITE_PERCENTAGE:
    #     frame_price = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    
    # else: 
    #     frame_price = 0
    
    grand_total = delivery + total #+ frame_price
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'artwork_count': artwork_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        # 'frame_price': frame_price,
    }

    return context
