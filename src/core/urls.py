from django.contrib import admin
from django.urls import path, include

from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('auth.urls', namespace='auth')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('user/', include('user.urls', namespace='user')),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),]