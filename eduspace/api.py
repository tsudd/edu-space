from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from .serializers import LoginSerializer, AccountSerializer, SubjectSerializer, TaskSerializer, TeacherSerializer
from rest_framework import status

from .models import Account, Subject, Teacher, Task


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

# Get Account API


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
            subjects = list(Subject.objects.filter(
                stud_class=request.user.id).select_related())
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
        subject = Subject.objects.get(pk=params['pk'])
        try:
            tasks = list(Task.objects.filter(subject=params['pk']))
        except:
            return
        return Response({
            "subject": self.nice_serializer(subject, context=self.get_serializer_context()).data,
            "tasks": self.serializer_class(tasks, many=True, context=self.get_serializer_context()).data
        })


class TaskList(generics.ListAPIView):
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


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
