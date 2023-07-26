from django.urls import path

from cv.views import CvCreateView, CvListView


app_name = 'cv'

urlpatterns = [
    path('list/', CvListView.as_view(), name='list'),
    path('create/', CvCreateView.as_view(), name='create'),
]
