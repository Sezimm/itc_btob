from rest_framework import serializers

from courses.serializers import PaymentSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'date_of_birth', 'email', 'phone_number', 'address', 'courses', 'group', 'status')

    def create(self, validated_data):
        courses = validated_data.pop('courses', [])
        student = Student.objects.create(**validated_data)
        student.courses.add(*courses)
        return student

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['payment'] = PaymentSerializer(instance.course_price.all(), many=True).data


class StudentListSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(view_name='student-detail', lookup_field='id')

    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'group', 'details']
