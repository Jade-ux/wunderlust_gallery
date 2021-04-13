  
from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified artwork to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    frame_option = None
    if 'artwork_frame' in request.POST:
        frame = request.POST['artwork_frame']
    cart = request.session.get('cart', {})

    # items_by_frame dictionary 
    # allows tracking of multiple sizes for single items
    if frame:
        if item_id in list(cart.keys()):
            if frame in cart[item_id]['items_by_frame'].keys():
                cart[item_id]['items_by_frame'][frame] += quantity
            else:
                cart[item_id]['items_by_frame'][frame] = quantity
        else:
            cart[item_id] = {'items_by_frame': {frame: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
