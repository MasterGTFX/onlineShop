from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/all', views.index),
    path('profile', views.profile),
    path('checkout', views.checkout),
    path('add_to_cart/<int:id>/<int:quantity>', views.add_to_cart),
    path('categories/<int:category>', views.index_category),
    path('base/', views.base, name='base'),
]