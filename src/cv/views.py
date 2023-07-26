from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)


class CvListView(LoginRequiredMixin, View):
    def get(self, request):
        cvs = request.user.profile.cvs.all()

        return render('cv/cv_list.html', {'cvs': cvs})


class CvView(View):
    pass
