from django import forms

from language.models import Language
from user.models import Profile


EditLanguageFormSet = forms.inlineformset_factory(
    Profile,
    Language,
    can_delete=True,
    extra=3,
    max_num=8,
    fields=[
        'name',
        'level',
    ],
)