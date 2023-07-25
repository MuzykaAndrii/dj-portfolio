from django import forms

from user.models import (
    Contact,
    Course,
    Employment,
    Profile,
    Education,
    Project,
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
        'data',
    ],
    can_delete=True,
    extra=0,
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


EditEmploymentFormSet = forms.inlineformset_factory(
    Profile,
    Employment,
    can_delete=True,
    extra=3,
    max_num=10,
    fields= [
        'company_name',
        'position',
        'description',
        'date_start',
        'date_end',
    ],
    widgets={
        'date_start': forms.widgets.DateInput(attrs={'type': 'date'}),
        'date_end': forms.widgets.DateInput(attrs={'type': 'date'}),
    }
)

EditCoursesFormSet = forms.inlineformset_factory(
    Profile,
    Course,
    can_delete=True,
    extra=4,
    max_num=20,
    fields= [
        'name',
        'certificate',
    ]
)

EditProjectsFormSet = forms.inlineformset_factory(
    Profile,
    Project,
    can_delete=True,
    extra=4,
    max_num=20,
    fields=[
        'name',
        'link',
        'source',
        'description',
    ]
)