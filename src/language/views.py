from user.generic import FormSetView
from user.mixins import ProfileRequiredMixin
from language.forms import EditLanguageFormSet


class LanguageView(ProfileRequiredMixin, FormSetView):
    related_field_name = 'profile'
    FormSet = EditLanguageFormSet
    template_name = 'language/languages.html'
    success_redirect = 'user:profile'