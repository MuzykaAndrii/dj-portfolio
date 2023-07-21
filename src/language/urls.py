from django.urls import path

from language.views import LanguageView


app_name = 'language'

urlpatterns = [
    path('edit/', LanguageView.as_view(), name='edit_languages'),
]
