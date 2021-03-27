from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('Name', max_length=30, default='Name')
    surname = models.CharField('Surname', max_length=30, default='Surname')
    name1 = models.CharField('Name 1', max_length=30, default='name1')
    email = models.CharField('Email', max_length=254, default='email')
    birth_date = models.DateField('Birth date')
    access = models.CharField('Access level', max_length=1)


class Teacher(User):
    status = models.CharField('Status', max_length=1, default='r')


class Class(models.Model):
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    number = models.IntegerField("Class number", default=-1)
    letter = models.CharField("Class letter", max_length=1)
    name = models.CharField("Class name", max_length=45)


class Student(User):
    stud_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)


class Subject(models.Model):
    name = models.CharField("Name", max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    description = models.CharField("Description", max_length=60)
    information = models.TextField(null=True, blank=True)
    stud_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)


class Task(models.Model):
    name = models.CharField("Name", max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    description = models.CharField("Description", max_length=100)
    creation_date = models.DateField('Creation date')
    information = models.TextField(null=True, blank=True)


class TheoryTask(Task):
    pass


class PracticeTask(Task):
    deadline = models.DateField('Deadline')


class Message(models.Model):
    class_receiver = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)
    text = models.TextField(null=True, blank=True)
    creation_date = models.DateField('Creation date')
    type = models.CharField("Type", max_length=1)

