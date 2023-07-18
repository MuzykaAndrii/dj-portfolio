from django.urls import path

from auth.views import (
    RegisterView,
    LoginView,
    LogoutView,
)


app_name = 'auth'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
