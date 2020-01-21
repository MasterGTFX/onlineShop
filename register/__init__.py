from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    user.profile.shopping_cart.clear()

@receiver(user_logged_out)
def on_logout(sender, user, request, **kwargs):
    user.profile.shopping_cart.clear()
