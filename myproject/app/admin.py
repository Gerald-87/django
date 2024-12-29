from django.contrib import admin
from .models import Teacher, Subject, Class, Student, Parent, Attendance, Grade, SchoolEvent

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(SchoolEvent)
