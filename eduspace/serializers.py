from rest_framework import serializers
from .models import MessageType, Student, Teacher, Class, Message, Subject, Task, Account, TeacherStatus
from django.contrib.auth import authenticate


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "name", "surname",
                  "birthDate", "email", "is_staff"]


class TeacherStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherStatus
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    status = TeacherStatusSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ["id", "user", "status"]


class ClassSerializer(serializers.ModelSerializer):
    curator = TeacherSerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"


class MessageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageType
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    stud_class = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["user", "stud_class"]


class MessageSerializer(serializers.ModelSerializer):
    class_receiver = ClassSerializer(read_only=True)
    sender = TeacherSerializer(read_only=True)
    creation_datetime = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    # type_ = MessageType

    class Meta:
        model = Message
        fields = ["id", "class_receiver", "text",
                  "creation_datetime", "type", "sender"]


class MessageSerializerNew(serializers.ModelSerializer):
    # type_ = MessageType

    class Meta:
        model = Message
        fields = ["id", "class_receiver", "text",
                  "creation_datetime", "type", "sender"]


class SubjectSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    stud_class = ClassSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "teacher", "description",
                  "information", "stud_class"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "subject", "description",
                  "creation_date", "deadline"]

# Loging serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Creadentials.")
