
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Assignment API",
        default_version='v1',
        description="Assignment API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-api/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('sentry-debug/', trigger_error),
    path('auth/',include('user.urls')),
    path('form/',include('user_form.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
