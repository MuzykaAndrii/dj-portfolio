from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('auth.urls', namespace='auth')),
    path('cv/', include('cv.urls', namespace='cv')),
    path('profile/', include('user.urls', namespace='user')),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)