from django.contrib import admin

from courses.models import Employee, Branch, Course, Group

admin.site.register(Employee)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Group)
