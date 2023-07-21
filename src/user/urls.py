from django.urls import include, path

from user.views import (
    ProfileView,
    CreateProfileView,
    EditProfileView,

    ContactView,
    EducationView,
)


app_name = 'user'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),

    path('contacts/edit/', ContactView.as_view(), name='edit_contacts'),
    path('education/edit/', EducationView.as_view(), name='edit_education'),
    path('language/', include('language.urls', namespace='language'))
]
