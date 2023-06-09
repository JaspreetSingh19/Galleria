"""galleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Project Galleria",
        default_version='Galleria',
        description="This Api is created to provide gallery images "
                    "and videos for the authenticated user.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="projectgalleria5@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('user/', include('account.urls')),
                  path('gallery/', include('gallery.urls')),
                  path('apidoc/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
