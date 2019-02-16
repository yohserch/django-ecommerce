from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import ContactForm, LoginForm, RegisterForm


def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "home.html", {})

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "contact_form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    
    return render(request, "contact/view.html", context)

def signin(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "login_form": login_form
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error al authenticar")
    return render(request, "auth/login.html", context)

def signout(request):
    logout(request)
    return render(request, "home.html", {})

def register(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "register_form": register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
        if new_user:
            return redirect("/")

    return render(request, "auth/register.html", context)