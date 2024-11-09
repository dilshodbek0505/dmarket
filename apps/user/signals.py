from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from apps.common.models import Cart

User = get_user_model()


@receiver(post_save, sender=User)
def attechment_cart_to_user(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user = instance)
    