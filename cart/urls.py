from django.urls import path
from . import views

"""URL for the cart page"""

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
]
