from django.contrib import admin
from .models import Category, Country, Artist, Artwork

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Artist)
admin.site.register(Artwork)
