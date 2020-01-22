from django.shortcuts import render, redirect
from .models import Product, Category, ProductInCart
from django.contrib.auth.decorators import login_required


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
    return render(request, "profile.html", {'profile_active': 'active'})


def about(request):
    return render(request, "about.html", {'about_active': 'active'})


def product(request, **kwargs):
    product = Product.objects.get(id=kwargs.get('id'))
    return render(request, "product.html", {'product': product})


def checkout(request):
    total_price = 0
    for product_in_cart in request.user.profile.shopping_cart.all():
        total_price += product_in_cart.product.price * product_in_cart.product_count
    return render(request, "checkout.html", {'total_price': total_price})


def check_quantity(request, product, product_in_cart):
    if product.quantity < product_in_cart.product_count:
        return False
    return True


@login_required(login_url='/login/')
def add_to_cart(request, **kwargs):
    categories = Category.objects.all()
    products = Product.objects.all()
    user_profile = request.user.profile
    product = Product.objects.get(id=kwargs.get('id'))
    for product_in_cart in user_profile.shopping_cart.all():
        if product_in_cart.product == product:
            product_in_cart.product_count += kwargs.get('quantity')
            if not check_quantity(request, product, product_in_cart):
                message = "We dont have {} of {} in stock!".format(product_in_cart.product_count, product.name)
                return render(request, "index.html",
                              {'categories': categories, 'products': products, 'categories_all_active': 'active',
                               'home_active': 'active', 'error_message': message})
            product_in_cart.save()
            user_profile.save()
            message = "Succesfully added {} of {} to cart :)".format(product_in_cart.product_count, product.name)
            return render(request, "index.html",
                          {'categories': categories, 'products': products, 'categories_all_active': 'active',
                           'home_active': 'active', 'info_message': message})
    product_in_cart = ProductInCart(product=product, product_count=kwargs.get('quantity'))
    if not check_quantity(request, product, product_in_cart):
        message = "We dont have {} of {} in stock!".format(product_in_cart.product_count, product.name)
        return render(request, "index.html",
                      {'categories': categories, 'products': products, 'categories_all_active': 'active',
                       'home_active': 'active', 'error_message': message})
    product_in_cart.save()
    user_profile.shopping_cart.add(product_in_cart)
    user_profile.save()
    message = "Succesfully added {} of {} to cart :)".format(product_in_cart.product_count, product.name)
    return render(request, "index.html",
                  {'categories': categories, 'products': products, 'categories_all_active': 'active',
                   'home_active': 'active', 'info_message': message})


@login_required(login_url='/login/')
def add_balance(request, **kwargs):
    request.user.profile.balance += kwargs.get('amount')
    request.user.profile.save()
    categories = Category.objects.all()
    products = Product.objects.all()
    message = "Succesfully added {} to balance :)".format(kwargs.get('amount'))
    return render(request, "index.html",
                  {'categories': categories, 'products': products, 'categories_all_active': 'active',
                   'home_active': 'active', 'info_message': message})


@login_required(login_url='/login/')
def remove_account(request, **kwargs):
    request.user.profile.delete()
    request.user.profile.save()
    request.user.delete()
    request.user.save()
    categories = Category.objects.all()
    products = Product.objects.all()
    error_message = "Your account has been removed! :("
    return render(request, "index.html",
                  {'categories': categories, 'products': products, 'categories_all_active': 'active',
                   'home_active': 'active', 'error_massage': error_message})


@login_required(login_url='/login/')
def remove_all(request, **kwargs):
    request.user.profile.shopping_cart.clear()
    return redirect(checkout)


@login_required(login_url='/login/')
def remove(request, **kwargs):
    product = Product.objects.get(id=kwargs.get('id'))
    for product_in_cart in request.user.profile.shopping_cart.all():
        if product_in_cart.product == product:
            product_in_cart_to_remove = product_in_cart
    if product_in_cart_to_remove:
        request.user.profile.shopping_cart.remove(product_in_cart_to_remove)
    return redirect(checkout)


@login_required(login_url='/login/')
def buy(request, **kwargs):
    total_price = 0
    for product_in_cart in request.user.profile.shopping_cart.all():
        total_price += product_in_cart.product.price * product_in_cart.product_count
    if request.user.profile.balance < total_price:
        message = "You dont have enough money! Your balance is {}. You can add funds at your profile".format(
            request.user.profile.balance)
        return render(request, "checkout.html", {'error_message': message})
    else:
        categories = Category.objects.all()
        products = Product.objects.all()
        request.user.profile.balance -= total_price
        request.user.profile.save()
        for product_in_cart in request.user.profile.shopping_cart.all():
            product = Product.objects.get(id=product_in_cart.product.id)
            product.quantity -= product_in_cart.product_count
            product.save()
        request.user.profile.shopping_cart.clear()
        message = "Thanks for shopping"
        return render(request, "index.html",
                      {'categories': categories, 'products': products, 'categories_all_active': 'active',
                       'home_active': 'active', 'info_message': message})
