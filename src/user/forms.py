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
        

ContactFormSet = forms.modelformset_factory(
    Contact,
    extra=6,
    fields=[
        'type',
        'link',
    ]
)
        