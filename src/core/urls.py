from django.contrib import admin
from django.urls import path, include

from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('user.urls', namespace='auth')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),]