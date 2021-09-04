from datetime import timedelta, datetime

from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=300)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    inn = models.CharField(max_length=14, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return self.full_name


class Branch(models.Model):
    REGIONS = (
        ('CH', 'Чуй'),
        ('TL', 'Талас'),
        ('IK', 'Иссык-Куль'),
        ('NR', 'Нарын'),
        ('DJ', 'Джалал-Абад'),
        ('OSH', 'Ош'),
        ('BT', 'Баткен')
    )
    title = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100, choices=REGIONS)
    address = models.CharField(max_length=200)
    admin = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='branches')

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='groups')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='groups')
    mentor = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='groups')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=self.course.duration * 7)
        return super(Group, self).save(*args, **kwargs)

