from django.shortcuts import redirect, render
from django.views import View

from user.forms import CreateProfileForm


class ProfileView(View):
    def get(self, request):
        return render(request, 'user/profile.html')

    def post(self, request):
        """updates user profile"""


class CreateProfileView(View):
    def get(self, request):
        """page with creation form"""
        if request.user.has_profile():
            # TODO: flash message
            return redirect('user:profile')

        profile_form = CreateProfileForm()
        return render(request, 'user/create_profile.html', {'profile_form': profile_form})
    
    def post(self, request):
        """creation form handler"""
        pass