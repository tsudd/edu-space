from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status

from .models import Account, Student, Subject, Teacher, Task


def get_student_or_teacher(user):
    if user.is_admin:
        return
    try:
        if user.is_staff:
            return Teacher.objects.get(user__id=user.id)
        return Student.objects.get(user__id=user.id)
    except:
        return None


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data
        _, token = AuthToken.objects.create(account)
        return Response({
            "account": AccountSerializer(account, context=self.get_serializer_context()).data,
            "token": token
        })


class AccountAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user


class TeachersAPI(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class SubjectList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        subjects = []
        params = dict(request.query_params)
        if request.user.is_admin:
            subjects = list(Subject.objects.all().select_related())
        elif request.user.is_staff:
            teacher = get_student_or_teacher(request.user)
            subjects = list(Subject.objects.filter(teacher=teacher.id))
        elif len(params) > 0:
            if 'id' in params:
                pk = int(params['id'][0])
                try:
                    subjects = [Subject.objects.get(pk=pk)]
                except:
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            stud = get_student_or_teacher(request.user)
            if stud is not None:
                subjects = list(Subject.objects.filter(
                    stud_class__id=stud.stud_class.id).select_related())
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({
            "subjects": self.serializer_class(subjects, many=True, context=self.get_serializer_context()).data
        })


class SubjectDetail(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Subject.objects.all()
    serializer_class = TaskSerializer
    nice_serializer = SubjectSerializer

    def get(self, request, *args, **kwargs):
        params = kwargs
        try:
            subject = Subject.objects.get(pk=params['pk'])
            if request.user.is_staff:
                teacher = get_student_or_teacher(request.user)
                assert teacher is not None and subject.teacher.id == teacher.id
            if not request.user.is_staff:
                student = get_student_or_teacher(request.user)
                assert student is not None and subject.stud_class.id == student.stud_class.id
            tasks = list(Task.objects.filter(subject=params['pk']))
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({
            "subject": self.nice_serializer(subject, context=self.get_serializer_context()).data,
            "tasks": self.serializer_class(tasks, many=True, context=self.get_serializer_context()).data
        })


class TaskList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        tasks = []
        if request.user.is_admin:
            tasks = list(Task.objects.all().select_related())
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({
            "tasks": self.serializer_class(tasks, many=True, context=self.get_serializer_context()).data
        })

    # make staff checker decorator
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().post(request, args, kwargs)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def put(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().put(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().delete(request, args, kwargs)


class MessageList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request, *args, **kwargs):
        messages = []
        if request.user.is_staff:
            teacher = get_student_or_teacher(request.user)
            messages += list(Message.objects.filter(sender__id=teacher.id).select_related())
            classes = list(Class.objects.filter(curator__id=teacher.id))
            for c in classes:
                messages += list(Message.objects.filter(
                    class_receiver__id=c.id).select_related())
        else:
            student = get_student_or_teacher(request.user)
            messages += list(Message.objects.filter(
                class_receiver__id=student.stud_class.id).select_related())

        return Response({
            "messages": self.serializer_class(messages, many=True, context=self.get_serializer_context()).data,
        })


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MessageSerializerNew
    queryset = Message.objects.all()

    def get(self, request, *args, **kwargs):
        messages = []
        if request.user.is_admin:
            messages = list(Message.objects.all().select_related())
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({
            "tasks": self.serializer_class(messages, many=True, context=self.get_serializer_context()).data
        })

    # make staff checker decorator
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().post(request, args, kwargs)
