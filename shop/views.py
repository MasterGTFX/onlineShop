from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html",
                  {'categories': categories, 'products': products, 'categories_all_active': 'active',
                   'home_active': 'active'})


def base(request):
    return render(request, "base.html", {'home_active': 'active'})


def index_category(request, **kwargs):
    categories = Category.objects.all()
    products = Product.objects.all()
    categories_id = [category.id for category in categories]
    if kwargs.get('category') in categories_id:
        products = [product for product in products if product.category.id == kwargs.get('category')]
    return render(request, "index.html", {'categories': categories, 'products': products, 'home_active': 'active'})
