from .models import Student, Teacher
from django.core.exceptions import ObjectDoesNotExist


class UserFactory(object):

    @staticmethod
    def get_student_or_teacher(uid: int, is_staff: bool, is_admin=False):
        if is_admin:
            return
        try:
            if is_staff:
                return Teacher.objects.get(user__id=uid)
            return Student.objects.get(user__id=uid)
        except ObjectDoesNotExist:
            return None
