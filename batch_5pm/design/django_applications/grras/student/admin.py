from django.contrib import admin

# Register your models here.
from .models import Student,Faculty,Course,Address

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Address)

