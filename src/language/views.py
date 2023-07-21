from user.generic import FormSetView
from language.forms import EditLanguageFormSet


class LanguageView(FormSetView):
    related_field_name = 'profile'
    FormSet = EditLanguageFormSet
    template_name = 'language/languages.html'
    success_redirect = 'user:profile'