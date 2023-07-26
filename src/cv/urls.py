from django.urls import path

from cv.views import CvListView


app_name = 'cv'

urlpatterns = [
    path('list/', CvListView.as_view(), name='list'),
]
