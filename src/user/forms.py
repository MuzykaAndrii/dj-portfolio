from django import forms

from user.models import (
    Contact,
    Profile,
)


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'surname',
            'date_birth',
            'birth_place',
            'residence_place',
        ]
        widgets = {
            'date_birth': forms.widgets.DateInput(attrs={'type': 'date'}),
        }


EditContactFormSet = forms.inlineformset_factory(
    Profile,
    Contact,
    fields=[
        'type',
        'link',
    ],
    can_delete=True,
    extra=5,
)
        