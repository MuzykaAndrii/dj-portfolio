from django.urls import path

from portfolio.views import index


app_name = 'portfolio'

urlpatterns = [
    path('index/', index, name='index'),
]