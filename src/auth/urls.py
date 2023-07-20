from django.urls import path

from auth.views import (
    RegisterView,
    LoginView,
    LogoutView,
    index,
)


app_name = 'auth'

urlpatterns = [
    path('', index, name='index'),

    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
