from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta: 
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):

    class Meta: 
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        'Country', null=True, blank=True, on_delete=models.SET_NULL)
    biography = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Artwork(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        'Country', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(
        'Artist', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image = models.ImageField()
    original_medium = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=254)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
