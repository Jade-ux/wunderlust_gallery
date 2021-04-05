from django.contrib import admin
from django.urls import path
from . import views

"""URL for the home page"""

urlpatterns = [
    path('', views.index, name='home'),
]
