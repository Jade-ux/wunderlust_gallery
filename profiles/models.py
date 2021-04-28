from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from artworks.models import Artwork


class UserProfile(models.Model):
    """
    User profile holds the default delivery information,
    order history and wishlist. 
    Each field is optional
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # For existing users, save the profile
    instance.userprofile.save()


    """
    Signal to add to wishlist
    """

    
class Wishlist(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True)
    wishlist_artwork = models.ForeignKey(
        Artwork, null=False, blank=False, on_delete=models.CASCADE)
    wishlist_path = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.wishlist_artwork.friendly_name
