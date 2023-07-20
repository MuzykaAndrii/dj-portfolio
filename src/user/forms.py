from django import forms

from user.models import (
    Contact,
    Profile,
    Education,
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


EditEducationFormSet = forms.inlineformset_factory(
    Profile,
    Education,
    can_delete=True,
    extra=3,
    max_num=4,
    fields=[
        'institution',
        'degree',
        'speciality',
        'date_start',
        'date_end',
    ],
    widgets={
        'date_start': forms.widgets.DateInput(attrs={'type': 'date'}),
        'date_end': forms.widgets.DateInput(attrs={'type': 'date'}),
    }
)
        