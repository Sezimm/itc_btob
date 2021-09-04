from django.db import models

from courses.models import Group, Course


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    courses = models.ManyToManyField(Course, through='ExtraTableForPayment', related_name='courses')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='students')
    status = models.BooleanField()

    def __str__(self):
        return self.full_name


class ExtraTableForPayment(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='courses_price')
    students = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='courses_price')
    payment = models.DecimalField(max_digits=10, decimal_places=2)


class StudentPayment(models.Model):
    students = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='student_payments')
    skidka = models.IntegerField()
    paid = models.DecimalField(max_digits=10, decimal_places=2)
    duty = models.DecimalField(max_digits=10, decimal_places=2)



