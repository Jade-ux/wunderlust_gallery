from django.urls import path
from . import views

"""URLs for the profile and wishlist page"""

urlpatterns = [
    path('', views.profile, name='profile')
]

#add wishlist URL
