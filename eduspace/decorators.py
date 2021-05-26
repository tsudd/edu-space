from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from rest_framework import status


def logged_staff(func):
    def wrapper(*args, **kwargs):
        req = args[1]
        if not req.user.is_staff:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return func(*args, **kwargs)
    return wrapper


class WrappedApiView(generics.RetrieveUpdateDestroyAPIView):
    @logged_staff
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)

    @logged_staff
    def put(self, request, *args, **kwargs):
        return super().put(request, args, kwargs)

    @logged_staff
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
