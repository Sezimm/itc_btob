from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from courses.models import Branch, Course, Group, Employee
from courses.serializers import BranchSerializer, CourseSerializer, GroupSerializer, EmployeeSerializer


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    search_fields = ['region', 'title', ]
    ordering_fields = ['region', ]


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    search_fields = ['title', ]
    ordering_fields = ['title', 'duration', 'payment']


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    search_fields = ['title', 'course']
    ordering_fields = ['title']


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    search_fields = ['full_name', 'position', ]
    ordering_fields = ['full_name', 'salary']


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'branches': reverse('branch-list', request=request, format=format),
        'courses': reverse('course-list', request=request, format=format),
        'group': reverse('group-list', request=request, format=format)
    })

