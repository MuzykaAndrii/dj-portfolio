from typing import Optional
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from user.forms import (
    ContactFormSet,
    CreateProfileForm,
)


class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth:login')
    
    def get(self, request):
        return render(request, 'user/profile.html')


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

        messages.success(request, "Profile sucessfully edited")
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

        messages.success(request, "Profile sucessfully created/edited")
        return redirect('user:profile')
    
    def test_func(self):
        return not self.request.user.has_profile()