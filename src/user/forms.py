from django import forms

from user.models import (
    Profile,
)


class DateInput(forms.DateInput):
    input_type = 'date'

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
            'date_birth': DateInput(),
        }