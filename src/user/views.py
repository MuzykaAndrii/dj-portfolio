from django.views import View


class ProfileView(View):
    def get(self, request):
        """shows user profile"""
        pass

    def post(self, request):
        """updates user profile"""