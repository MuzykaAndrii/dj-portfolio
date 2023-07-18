from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from user.forms import (
    UserRegisterForm,
    UserLoginForm
)


def register_user(request):
    if not request.method == "POST":
        form = UserRegisterForm()
        return render(request, "user/register.html", {"form": form})

    form = UserRegisterForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Registration error")
        return render(request, "user/register.html", {"form": form})

    form.save()
    messages.success(request, "User registration successful")
    return redirect("login_user")


def login_user(request):
    if not request.method == "POST":
        form = UserLoginForm()
        return render(request, "user/login.html", {"form": form})

    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"{user.username} successfully logged in.")
        return redirect("index")

    return render(request, "user/login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect("login_user")
