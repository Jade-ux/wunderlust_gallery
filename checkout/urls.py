from django.urls import path
from . import views

"""URL for the checkout page"""

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>',
        views.checkout_success, name='checkout_success'
        ),
]
