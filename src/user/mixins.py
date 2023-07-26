from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib import messages
from django.shortcuts import redirect


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = 'auth:login'


class ProfileRequiredMixin(MyLoginRequiredMixin, UserPassesTestMixin):    
    def test_func(self):
        return self.request.user.has_profile()
    
    def handle_no_permission(self):
        messages.warning(self.request, "You're haven't profile yet, please create using form below.")
        return redirect('user:create_profile')