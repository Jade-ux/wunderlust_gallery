from django.contrib import admin
from django.urls import path
from . import views

"""URL for the cart page"""

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
]
