from django.contrib import admin
from .models import Student  # Fixed import statement

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "number"]
