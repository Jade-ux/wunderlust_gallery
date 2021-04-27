from django.urls import path
from . import views

"""URLs for the profile and wishlist page"""

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]

#add wishlist URL
