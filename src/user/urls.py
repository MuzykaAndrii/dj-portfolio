from django.urls import include, path

from user.views import (
    CourseView,
    CoursesView,
    ProfileView,
    CreateProfileView,
    EditProfileView,

    ContactView,
    EducationView,
    EmploymentView,
    ProjectsView,
)


app_name = 'user'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),

    path('contacts/edit/', ContactView.as_view(), name='edit_contacts'),
    path('education/edit/', EducationView.as_view(), name='edit_education'),
    path('employment/edit', EmploymentView.as_view(), name='edit_employment'),
    path('courses/edit/', CoursesView.as_view(), name='edit_courses'),
    path('projects/edit/', ProjectsView.as_view(), name='edit_projects'),

    path('courses/show/<int:course_pk>/', CourseView.as_view(), name='view_course'),

    path('language/', include('language.urls', namespace='language')),
]
