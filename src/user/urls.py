from django.urls import path

from user.views import (
    ProfileView,
)


app_name = 'user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
]
