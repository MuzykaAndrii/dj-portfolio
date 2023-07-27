from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.db.utils import IntegrityError
from django.db import transaction

from user.mixins import MyLoginRequiredMixin, ProfileRequiredMixin
from cv.forms import CvForm, SkillsFormSet
from cv.models import Skill, CV


class CvListView(MyLoginRequiredMixin, View):
    def get(self, request):
        cvs = request.user.profile.cvs.all()

        return render(request, 'cv/cv_list.html', {'cvs': cvs})


class CvCreateView(ProfileRequiredMixin, View):
    def get(self, request):
        cv_form = CvForm()
        skills_formset = SkillsFormSet(queryset=Skill.objects.none())

        context = {
            'cv_form': cv_form,
            'skills_formset': skills_formset,
        }
        return render(request, 'cv/cv_manage.html', context)

    def post(self, request):
        cv_form = CvForm(data=request.POST, files=request.FILES)
        skills_formset = SkillsFormSet(data=request.POST)

        if not (cv_form.is_valid() and skills_formset.is_valid()):
            messages.error(request, 'Please, enter the correct data')
            return render(request, 'cv/cv_manage.html', {'cv_form': cv_form, 'skills_formset': skills_formset})
        
        cv = cv_form.save(commit=False)
        cv.profile = request.user.profile

        try:
            with transaction.atomic():
                cv.save()
                skills = self.get_bulk_skills(skills_formset, cv)
                Skill.objects.bulk_create(skills)
        
        except IntegrityError as e:
            messages.error(request, f'Failed to save: {e}')
            return render(request, 'cv/cv_manage.html', {'cv_form': cv_form, 'skills_formset': skills_formset})
        
        # TODO: redirect to cv item page
        messages.success(request, 'CV created successfully')
        return redirect('cv:list')
    
    def get_bulk_skills(self, skills_formset: SkillsFormSet, cv: CV) -> list[Skill]:
        """Unpack skill objects from formset, applying to each given cv instance"""
        skills = list()

        for skill_form in skills_formset:
            skill_obj = skill_form.save(commit=False)
            skill_obj.cv = cv
            skills.append(skill_obj)
        
        return skills
            