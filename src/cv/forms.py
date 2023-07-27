from django import forms

from cv.models import (
    CV,
    Skill,
)


class MyImageInput(forms.ClearableFileInput):
    clear_checkbox_label = "Clear"
    initial_text = "Current avatar"
    input_text = "Set cv avatar"
    template_name = 'cv/widgets/image_widget.html'


class CvForm(forms.ModelForm):
    class Meta:
        model = CV
        exclude = [
            'profile',
        ]

        widgets={
            'avatar': MyImageInput,
        }


SkillsFormSet = forms.modelformset_factory(
    Skill,
    can_delete=True,
    extra=1,
    exclude=[
        'cv',
    ],
)