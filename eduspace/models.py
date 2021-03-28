from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('Name', max_length=30, default='Name')
    surname = models.CharField('Surname', max_length=30, default='Surname')
    name1 = models.CharField('Name 1', max_length=30, default='name1')
    email = models.CharField('Email', max_length=254, default='email')
    birth_date = models.DateField('Birth date')
    access = models.CharField('Access level', max_length=1)

    def __str__(self):
        return f"User {self.name} {self.surname} with {self.access} access"


class Teacher(User):
    status = models.CharField('Status', max_length=1, default='r')

    def __str__(self):
        return f"Teacher {self.name} {self.surname} with {self.access} access"


class Class(models.Model):
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    number = models.IntegerField("Class number", default=-1)
    letter = models.CharField("Class letter", max_length=1)

    def __str__(self):
        return f"Class {self.number} {self.letter}"


class Student(User):
    stud_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Student {self.name} {self.surname} from {self.stud_class}"


class Subject(models.Model):
    name = models.CharField("Name", max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    description = models.CharField("Description", max_length=60)
    information = models.TextField(null=True, blank=True)
    stud_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Subject {self.name} in {self.stud_class}"


class Task(models.Model):
    name = models.CharField("Name", max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    description = models.CharField("Description", max_length=250)
    creation_date = models.DateField('Creation date')

    def __str__(self):
        return f"Task {self.name} {self.subject} {self.creation_date}."


class TheoryTask(Task):
    def __str__(self):
        return f"TheoryTask from {super.__str__(self)}"


class PracticeTask(Task):
    deadline = models.DateField('Deadline')

    def __str__(self):
        return f"PracticeTask {self.name} in {self.subject}"


class Message(models.Model):
    class_receiver = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)
    text = models.TextField(null=True, blank=True)
    creation_date = models.DateField('Creation date')
    type = models.CharField("Type", max_length=1)

    def __str__(self):
        return f"Message for {self.class_receiver} from {self.creation_date} of {self.type}"

