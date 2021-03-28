from django.contrib import admin

from .models import Student
from .models import Teacher
from .models import Class
from .models import Subject
from .models import Message
from .models import TheoryTask
from .models import PracticeTask


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', "surname", "name1", "birth_date")
    list_display_links = ("name", "surname")
    search_fields = ("name", "surname")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', "surname", "name1", "birth_date", "status")
    list_display_links = ("name", "surname")
    search_fields = ("name", "surname", "status")


class ClassAdmin(admin.ModelAdmin):
    list_display = ("number", "letter", "curator")
    list_display_links = ("number", "curator")
    search_fields = ("number", "curator")


class TheoryTaskAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "creation_date")
    list_display_links = ("name", "subject")
    search_fields = ("name", "subject")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "stud_class", "description")
    list_display_links = ("name", "teacher", "stud_class")
    search_fields = ("name", "teacher", "stud_class")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("class_receiver", "creation_date")
    list_display_links = ("class_receiver", "creation_date")
    search_fields = ("class_receiver", "creation_date")


class PracticeTaskAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "creation_date", "deadline")
    list_display_links = ("name", "subject")
    search_fields = ("name", "subject", "deadline")


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TheoryTask, TheoryTaskAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(PracticeTask, PracticeTaskAdmin)
admin.site.register(Class, ClassAdmin)

# Register your models here.
