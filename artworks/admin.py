from django.contrib import admin
from .models import Category, Country, Artist, Artwork

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'category',
        'country',
    )

class ArtworkAdmin(admin.ModelAdmin):
    list_display =(
        'friendly_name',
        'name',
        'artist',
        'category',
        'country',
        'price',
        'featured',
    )

    ordering = ('artist', 'friendly_name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
