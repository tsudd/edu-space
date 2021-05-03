from rest_framework import serializers
from .models import Student, Teacher, Class, Message, Subject, Task, Account


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ["user", "stud_class"]


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ["user", "status"]


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ["curator", "number", "letter"]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ["class_receiver", "text", "creation_datetime", "type", "sender"]


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ["name", "teacher", "description", "information", "stud_class"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "subject", "description", "creation_date", "deadline"]


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "name", "surname", "birthDate", "email"]
