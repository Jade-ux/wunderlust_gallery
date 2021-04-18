from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# from the Boutique Ado project
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when lineitem is updated or created
    """
    instance.order.update_total()


# from the Boutique Ado project
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total when lineitem is deleted
    """
    instance.order.update_total()
