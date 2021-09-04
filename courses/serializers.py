from rest_framework import serializers

from courses.models import Course, Group, Branch, Employee
from students.models import ExtraTableForPayment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'duration', 'payment')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        exclude = ('end_date', )


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('region', 'title', 'address', 'admin')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('full_name', 'date_of_birth', 'position', 'salary', 'inn', 'email', 'phone_number')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraTableForPayment
        fields = ('courses', 'price', )
