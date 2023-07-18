from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views import View

from auth.forms import (
    UserRegisterForm,
    UserLoginForm
)


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "auth/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if not form.is_valid():
            messages.error(request, "Registration error")
            return render(request, "auth/register.html", {"form": form})
        
        form.save()
        messages.success(request, "User registration successful")
        return redirect("auth:login")


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "auth/login.html", {"form": form})
    
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"{user.username} successfully logged in.")
            return redirect("portfolio:index")

        return render(request, "auth/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logged out.")
        return redirect("auth:login")