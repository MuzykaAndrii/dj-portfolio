from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import CreateProfileForm


class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth:login')
    
    def get(self, request):
        return render(request, 'user/profile.html')

    def post(self, request):
        """updates user profile"""


class CreateProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth:login')
    
    def get(self, request):
        """page with creation form"""
        if request.user.has_profile():
            messages.warning(request, "Youre already have a profile")
            return redirect('user:profile')

        profile_form = CreateProfileForm()
        return render(request, 'user/create_profile.html', {'profile_form': profile_form})
    
    def post(self, request):
        """creation form handler"""
        profile_form = CreateProfileForm(request.POST)

        if not profile_form.is_valid():
            messages.error(request, "Error during creation profile")
            return render(request, 'user/create_profile.html', {'profile_form': profile_form})
        
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile_form.save()

        messages.success(request, "Profile sucessfully created")
        return redirect('user:profile')