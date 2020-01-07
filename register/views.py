from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = response.POST['username']
            password = response.POST['password1']
            user = authenticate(username=username, password=password)
            login(response, user)
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form": form, 'login_active': 'active'})



