from dataclasses import field
from django.contrib import admin
from .models import Track, Student
# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Info', {'fields': ['fname', 'lname', 'age']}],
        ['Scholarship Info', {'fields': ['student_track']}],
    )
    list_display = ('fname', 'lname', 'age', 'student_track', 'is_adult')
    search_fields = ('fname', 'lname', 'age', 'student_track__track_name')
    list_filter = ('student_track__track_name',)

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 2

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)
