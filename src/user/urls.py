from django.urls import path

from user.views import (
    ProfileView,
    CreateProfileView,
    EditProfileView,

    EditContactView,
)


app_name = 'user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/create', CreateProfileView.as_view(), name='create_profile'),
    path('profile/edit', EditProfileView.as_view(), name='edit_profile'),

    path('profile/contacts/edit', EditContactView.as_view(), name='edit_contacts'),
]
