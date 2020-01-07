from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/all', views.index),
    path('categories/<int:category>', views.index_category),
    path('base/', views.base, name='base'),
]