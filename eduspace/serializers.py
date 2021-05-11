from rest_framework import serializers
from .models import Student, Teacher, Class, Message, Subject, Task, Account, TeacherStatus
from django.contrib.auth import authenticate


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "name", "surname", "birthDate", "email"]


class TeacherStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherStatus
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    status_set = serializers.PrimaryKeyRelatedField(
        source="status", read_only=True)

    class Meta:
        model = Teacher
        fields = ["user", "status_set"]


class ClassSerializer(serializers.ModelSerializer):
    curator = TeacherSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ["curator", "number", "letter"]


class StudentSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    stud_class = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["user", "stud_class"]


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ["class_receiver", "text",
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
        fields = ["name", "subject", "description",
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
