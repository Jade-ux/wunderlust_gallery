from django.urls import path
from . import views

"""URL for the checkout page"""

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
