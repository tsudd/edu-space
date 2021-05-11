from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import LoginSerializer, AccountSerializer, SubjectSerializer

from .models import Account, Subject


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


class SubjectsAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SubjectSerializer

    # queryset = Subject.objects.get()

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        return Response({
            "subjects": subjects
        })
