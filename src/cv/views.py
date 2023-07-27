from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db.utils import IntegrityError
from django.db import transaction
from django.core.exceptions import PermissionDenied

from user.mixins import MyLoginRequiredMixin, ProfileRequiredMixin
from cv.forms import CvForm, SkillsInlineFormSet, SkillsModelFormSet
from cv.models import Skill, CV


class CvListView(MyLoginRequiredMixin, View):
    def get(self, request):
        cvs = request.user.profile.cvs.all()

        return render(request, 'cv/cv_list.html', {'cvs': cvs})


class CvCreateView(ProfileRequiredMixin, View):
    def get(self, request):
        cv_form = CvForm()
        skills_formset = SkillsModelFormSet(queryset=Skill.objects.none())

        context = {
            'cv_form': cv_form,
            'skills_formset': skills_formset,
        }
        return render(request, 'cv/cv_manage.html', context)

    def post(self, request):
        cv_form = CvForm(data=request.POST, files=request.FILES)
        skills_formset = SkillsModelFormSet(data=request.POST)

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
    
    def get_bulk_skills(self, skills_formset: SkillsModelFormSet, cv: CV) -> list[Skill]:
        """Unpack skill objects from formset, applying to each given cv instance"""
        skills = list()

        for skill_form in skills_formset:
            skill_obj = skill_form.save(commit=False)
            skill_obj.cv = cv
            skills.append(skill_obj)
        
        return skills


class CvEditView(ProfileRequiredMixin, View):
    def get(self, request, cv_pk):
        if not request.user.profile.is_owner_of_cv(cv_pk):
            raise PermissionDenied

        cv_obj = get_object_or_404(CV.objects.prefetch_related('skills'), pk=cv_pk)

        cv_form = CvForm(instance=cv_obj)
        skills_formset = SkillsInlineFormSet(instance=cv_obj)

        context = {
            'cv_form': cv_form,
            'skills_formset': skills_formset,
            'edit': True,
        }
        return render(request, 'cv/cv_manage.html', context)

    def post(self, request, cv_pk):
        pass
            