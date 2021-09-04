from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from students.models import Student
from students.serializers import StudentSerializer, StudentListSerializer


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ['status', 'group']
    search_fields = ['full_name', 'email']
    ordering_fields = ['full_name', '']

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        return self.serializer_class

