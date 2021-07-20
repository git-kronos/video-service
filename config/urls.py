from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls'),  name='courses'),
    path('memberships/', include('memberships.urls'),  name='memberships'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
