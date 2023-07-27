from django.urls import path

from cv.views import (
    CvCreateView,
    CvDeleteView,
    CvEditView,
    CvListView,
)


app_name = 'cv'

urlpatterns = [
    path('list/', CvListView.as_view(), name='list'),
    path('create/', CvCreateView.as_view(), name='create'),
    path('edit/<int:cv_pk>/', CvEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', CvDeleteView.as_view(), name='delete'),
]
