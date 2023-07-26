from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import (
    UserPassesTestMixin
)

from user.forms import (
    CreateProfileForm,
    EditContactFormSet,
    EditCoursesFormSet,
    EditEducationFormSet,
    EditEmploymentFormSet,
    EditProjectsFormSet,
)
from user.generic import FormSetView
from user.models import Course, Profile
from user.mixins import (
    ProfileRequiredMixin,
    MyLoginRequiredMixin,
)


class ProfileView(ProfileRequiredMixin, View):    
    def get(self, request):        
        profile = Profile.objects.prefetch_related(
            'contacts',
            'education_set',
            'employments',
            'courses',
            'projects',
            'languages',
        ).get(user=request.user)

        context = {
            'contacts': profile.contacts.all(),
            'education_set': profile.education_set.all(),
            'languages': profile.languages.all(),
            'employments': profile.employments.all(),
            'courses': profile.courses.all(),
            'projects': profile.projects.all(),
        }

        return render(request, 'user/profile.html', context)


class EditProfileView(ProfileRequiredMixin, View):
    """view for editing existing profile"""

    def get(self, request):
        """page with update form"""
        profile_form = CreateProfileForm(instance=request.user.profile)

        return render(request, 'user/edit_profile.html', {'profile_form': profile_form})
    
    def post(self, request):
        """update form handler"""
        profile_form = CreateProfileForm(request.POST, instance=request.user.profile)

        if not profile_form.is_valid():
            messages.error(request, "Error during editing profile")
            return render(request, 'user/edit_profile.html', {'profile_form': profile_form})

        profile_form.save()

        messages.success(request, "Profile successfully edited")
        return redirect('user:profile')


class CreateProfileView(UserPassesTestMixin, View):
    """View to create a new profile"""

    def get(self, request):
        """page with creation form"""
        profile_form = CreateProfileForm()
        return render(request, 'user/edit_profile.html', {'profile_form': profile_form})
    
    def post(self, request):
        """creation form handler"""
        profile_form = CreateProfileForm(request.POST)

        if not profile_form.is_valid():
            messages.error(request, "Error during creation profile")
            return render(request, 'user/edit_profile.html', {'profile_form': profile_form})
        
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile_form.save()

        messages.success(request, "Profile successfully created")
        return redirect('user:profile')
    
    def test_func(self):
        return not self.request.user.has_profile()


class ContactView(ProfileRequiredMixin, FormSetView):
    related_field_name = 'profile'
    FormSet = EditContactFormSet
    template_name = 'user/contacts.html'
    success_redirect = 'user:profile'


class EducationView(ProfileRequiredMixin, FormSetView):
    related_field_name = 'profile'
    FormSet = EditEducationFormSet
    template_name = 'user/education.html'
    success_redirect = 'user:profile'


class EmploymentView(ProfileRequiredMixin, FormSetView):
    related_field_name = 'profile'
    FormSet = EditEmploymentFormSet
    template_name = 'user/employment.html'
    success_redirect = 'user:profile'


class CoursesView(ProfileRequiredMixin, FormSetView):
    related_field_name = 'profile'
    FormSet = EditCoursesFormSet
    template_name = 'user/courses.html'
    success_redirect = 'user:profile'


class ProjectsView(ProfileRequiredMixin, FormSetView):
    related_field_name = 'profile'
    FormSet = EditProjectsFormSet
    template_name = 'user/projects.html'
    success_redirect = 'user:profile'


class CourseView(View):
    def get(self, request, course_pk):
        course = get_object_or_404(Course.objects.select_related('profile'), pk=course_pk)

        return render(request, 'user/course_item.html', {'course': course})