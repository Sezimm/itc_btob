from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.views import BranchViewSet, CoursesViewSet, GroupViewSet, EmployeeViewSet

router_courses = DefaultRouter()
router_courses.register('courses', CoursesViewSet)

router_branches = DefaultRouter()
router_branches.register('branches', BranchViewSet)

router_groups = DefaultRouter()
router_groups.register('groups', GroupViewSet)

router_employee = DefaultRouter()
router_employee.register('employees', EmployeeViewSet)


urlpatterns = [
    path('', include(router_courses.urls)),
    path('', include(router_branches.urls)),
    path('', include(router_groups.urls)),
    path('', include(router_employee.urls)),
]
