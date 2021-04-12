from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=254, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    name = models.CharField("Name", max_length=30, default='UNNAMED USER', blank=True)
    surname = models.CharField("Surname", max_length=30, default='', blank=True)
    birthDate = models.DateField(verbose_name="birth date")
    name1 = models.CharField(max_length=30, default='', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", ]

    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class TeacherStatus(models.Model):
    status_name = models.CharField("Status name", max_length=30)
    abbr = models.CharField("Abbreviation", default=None, max_length=3)

    def __str__(self):
        return self.status_name


class Teacher(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    status = models.ForeignKey(TeacherStatus, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.user.email


class Class(models.Model):
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    number = models.IntegerField("Class number", default=-1)
    letter = models.CharField("Class letter", max_length=1)

    def __str__(self):
        return f"Class {self.number} {self.letter}"


class Student(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    stud_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.email


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


class MessageType(models.Model):
    type_name = models.CharField("Type name", default=None, max_length=30)
    char = models.CharField("Type char", default=None, max_length=1)

    def __str__(self):
        return f"{self.type_name} message"


class Message(models.Model):
    class_receiver = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)
    text = models.TextField(null=True, blank=True)
    creation_date = models.DateField('Creation date')
    type = models.ForeignKey(MessageType, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return f"Message for {self.class_receiver} from {self.creation_date} of {self.type}"
