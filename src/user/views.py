from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
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


class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth:login')
    
    def get(self, request):
        if not request.user.has_profile():
            messages.warning(request, "You're haven't profile yet, please create using form below.")
            return redirect('user:create_profile')
        
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


class EditProfileView(LoginRequiredMixin, View):
    """view for editing existing profile,
    uses same template as create profile view
    """
    login_url = reverse_lazy('auth:login')

    def _render_page(self, request, form):
        return render(request, 'user/edit_profile.html', {'profile_form': form})

    def get(self, request):
        """page with update form"""
        profile_form = CreateProfileForm(instance=request.user.profile)

        return self._render_page(request, profile_form)
    
    def post(self, request):
        """update form handler"""
        profile_form = CreateProfileForm(request.POST, instance=request.user.profile)

        if not profile_form.is_valid():
            messages.error(request, "Error during editing profile")
            return self._render_page(request, profile_form)
        
        profile_form.save()

        messages.success(request, "Profile successfully edited")
        return redirect('user:profile')


class CreateProfileView(UserPassesTestMixin, EditProfileView):
    """View to create a new profile, uses the
    same template as edit profile view"""

    def get(self, request):
        """page with creation form"""
        profile_form = CreateProfileForm()
        return self._render_page(request, profile_form)
    
    def post(self, request):
        """creation form handler"""

        profile_form = CreateProfileForm(request.POST)

        if not profile_form.is_valid():
            messages.error(request, "Error during creation profile")
            return self._render_page(request, profile_form)
        
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile_form.save()

        messages.success(request, "Profile successfully created/edited")
        return redirect('user:profile')
    
    def test_func(self):
        return not self.request.user.has_profile()


class ContactView(FormSetView):
    related_field_name = 'profile'
    FormSet = EditContactFormSet
    template_name = 'user/contacts.html'
    success_redirect = 'user:profile'


class EducationView(FormSetView):
    related_field_name = 'profile'
    FormSet = EditEducationFormSet
    template_name = 'user/education.html'
    success_redirect = 'user:profile'


class EmploymentView(FormSetView):
    related_field_name = 'profile'
    FormSet = EditEmploymentFormSet
    template_name = 'user/employment.html'
    success_redirect = 'user:profile'


class CoursesView(FormSetView):
    related_field_name = 'profile'
    FormSet = EditCoursesFormSet
    template_name = 'user/courses.html'
    success_redirect = 'user:profile'


class ProjectsView(FormSetView):
    related_field_name = 'profile'
    FormSet = EditProjectsFormSet
    template_name = 'user/projects.html'
    success_redirect = 'user:profile'


class CourseView(View):
    def get(self, request, course_pk):
        course = get_object_or_404(Course.objects.select_related('profile'), pk=course_pk)

        return render(request, 'user/course_item.html', {'course': course})