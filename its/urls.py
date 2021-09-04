"""its URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from courses.views import api_root
from students.views import StudentViewSet, StudentListView

router = DefaultRouter()
router.register('students', StudentViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='BtoB API',
        default_version='v1',
        description='BtoB API documentation'
    ), public=True
)

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('courses.urls')),
    path('api/v1/', include('dds.urls')),
    path('api/v1/docs/', schema_view.with_ui()),
    path('api/v1/students/', StudentListView.as_view(), name='student-list'),
]
