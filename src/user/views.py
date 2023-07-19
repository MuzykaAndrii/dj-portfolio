from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request):
        return render(request, 'user/profile.html')

    def post(self, request):
        """updates user profile"""