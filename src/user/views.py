from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import (
    ContactFormSet,
    CreateProfileForm,
)


class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth:login')
    
    def get(self, request):
        return render(request, 'user/profile.html')


class CreateProfileView(LoginRequiredMixin, View):
    """View to create a new profile"""
    login_url = reverse_lazy('auth:login')

    def get(self, request):
        """page with creation form"""
        profile_form = CreateProfileForm()

        return render(request, 'user/create_profile.html', {'profile_form': profile_form})
    
    def post(self, request):
        """creation form handler"""
        profile_form = CreateProfileForm(request.POST)

        if not profile_form.is_valid():
            messages.error(request, "Error during creation/editing profile")
            return render(request, 'user/create_profile.html', {'profile_form': profile_form})
        
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile_form.save()

        messages.success(request, "Profile sucessfully created/edited")
        return redirect('user:profile')


class EditProfileView(LoginRequiredMixin, View):
    """view for editing existing profile, uses same template as create view"""
    login_url = reverse_lazy('auth:login')
    
    def get(self, request):
        """page with update form"""
        profile_form = CreateProfileForm(instance=request.user.profile)

        return render(request, 'user/create_profile.html', {'profile_form': profile_form})
    
    def post(self, request):
        """update form handler"""
        profile_form = CreateProfileForm(request.POST, instance=request.user.profile)

        if not profile_form.is_valid():
            messages.error(request, "Error during editing profile")
            return render(request, 'user/create_profile.html', {'profile_form': profile_form})
        
        profile_form.save()

        messages.success(request, "Profile sucessfully edited")
        return redirect('user:profile')