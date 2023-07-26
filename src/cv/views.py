from django.contrib import messages
from django.shortcuts import render
from django.views import View

from cv.forms import CvForm, SkillsFormSet
from user.mixins import MyLoginRequiredMixin


class CvListView(MyLoginRequiredMixin, View):
    def get(self, request):
        cvs = request.user.profile.cvs.all()

        return render(request, 'cv/cv_list.html', {'cvs': cvs})


class CvCreateView(MyLoginRequiredMixin, View):
    def get(self, request):
        cv_form = CvForm()
        skills_formset = SkillsFormSet()

        context = {
            'cv_form': cv_form,
            'skills_formset': skills_formset,
        }
        return render(request, 'cv/cv_manage.html', context)

    def post(self, request):
        pass