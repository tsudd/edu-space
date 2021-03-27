from django.contrib import admin

from .models import Student
from .models import Teacher
from .models import Class
from .models import Subject
from .models import Message
from .models import TheoryTask
from .models import PracticeTask

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TheoryTask)
admin.site.register(Subject)
admin.site.register(Message)
admin.site.register(PracticeTask)
admin.site.register(Class)

# Register your models here.
