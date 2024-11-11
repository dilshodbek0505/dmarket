from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.common.models import Rating, Product, ProductSize

@receiver(post_save, sender=Rating)
def add_rating(sender, instance, created, **kwargs):
    if created:
        product = instance.product

        ratings = product.ratings.all()
        if ratings.exists():
            total_rating = sum(r.rating for r in ratings)
            product.rating = total_rating / ratings.count()
            product.save()        