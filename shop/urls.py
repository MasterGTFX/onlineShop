from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/all', views.index),
    path('profile', views.profile),
    path('about', views.about),
    path('checkout', views.checkout),
    path('add_to_cart/<int:id>/<int:quantity>', views.add_to_cart),
    path('remove/all', views.remove_all),
    path('remove/<int:id>', views.remove),
    path('id/<int:id>', views.product),
    path('add_balance/<int:amount>', views.add_balance),
    path('remove_account/', views.remove_account),
    path('buy', views.buy),
    path('categories/<int:category>', views.index_category),
    path('base/', views.base, name='base'),
]