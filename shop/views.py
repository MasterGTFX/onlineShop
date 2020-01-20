from django.shortcuts import render, redirect
from .models import Product, Category, ProductInCart
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
def index(request, **kwargs):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html",
                  {'categories': categories, 'products': products, 'categories_all_active': 'active',
                   'home_active': 'active', 'error_message': kwargs.get('error_message')})


def base(request):
    return render(request, "base.html", {'home_active': 'active'})


def index_category(request, **kwargs):
    categories = Category.objects.all()
    products = Product.objects.all()
    categories_id = [category.id for category in categories]
    if kwargs.get('category') in categories_id:
        products = [product for product in products if product.category.id == kwargs.get('category')]
    return render(request, "index.html", {'categories': categories, 'products': products, 'home_active': 'active',
                                          "active_category": kwargs.get('category')})


def profile(request):
    products = Product.objects.all()
    return render(request, "profile.html", {})


def checkout(request):
    products = Product.objects.all()
    return render(request, "checkout.html", {})


@login_required(login_url='/login/')
def add_to_cart(request, **kwargs):
    user_profile = request.user.profile

    product = Product.objects.get(id=kwargs.get('id'))
    if product.quantity < kwargs.get('quantity'):
        message = "We dont have {} {} in stock".format(kwargs.get('quantity'), product.name)
        return redirect(index, error_message=message)
    product_in_cart = ProductInCart(product=product, product_count=kwargs.get('quantity'))
    product_in_cart.save()
    user_profile.shopping_cart.add(product_in_cart)
    user_profile.save()
    #user_profile.shopping_cart.clear()
    return redirect(index)
