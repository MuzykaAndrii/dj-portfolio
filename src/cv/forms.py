from django import forms

from cv.models import (
    CV,
    Skill,
)


class CvForm(forms.ModelForm):
    class Meta:
        model = CV
        exclude = [
            'profile',
        ]


SkillsFormSet = forms.modelformset_factory(
    Skill,
    can_delete=True,
    extra=1,
    exclude=[
        'cv',
    ],
)