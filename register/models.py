from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from shop.models import ProductInCart


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)
    shopping_cart = models.ManyToManyField(ProductInCart, blank=True)

    @property
    def shopping_cart_price(self):
        cart_sum = 0
        for product_in_cart in self.shopping_cart:
            cart_sum += product_in_cart.product.price * product_in_cart.product_count
        return cart_sum

    def __str__(self):
        return "{}".format(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
