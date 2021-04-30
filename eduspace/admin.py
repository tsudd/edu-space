from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Student
from .models import Teacher
from .models import Class
from .models import Subject
from .models import Message
from .models import Task
from .models import MessageType
from .models import Account
from .models import TeacherStatus


class AccountCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = (
            'email',
            'birthDate',
            'username',
            'is_staff',
            "is_active",
            "is_superuser",
            'name',
            'surname',
            'name1',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password1 = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = (
            'email',
            'username',
            'password',
            'birthDate',
            'name',
            'surname',
            'name1',
            'is_active',
            'is_admin',
            "is_superuser"
        )


class AccountAdmin(UserAdmin):
    # The forms to add and change user instances
    form = AccountChangeForm
    add_form = AccountCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'birthDate', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        ('Personal info', {'fields': ('birthDate', 'name', 'surname', 'name1')}),
        ('Permissions', {'fields': ('is_admin', "is_staff", "is_active", "is_superuser")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'birthDate', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class ClassAdmin(admin.ModelAdmin):
    list_display = ("number", "letter", "curator")
    list_display_links = ("number", "curator")
    search_fields = ("number", "curator")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "creation_date", "description")
    list_display_links = ("name", "subject")
    search_fields = ("name", "subject")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "stud_class", "description", "information")
    list_display_links = ("name", "teacher", "stud_class")
    search_fields = ("name", "teacher", "stud_class")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("class_receiver", "creation_datetime", "text", "type", "sender")
    list_display_links = ("class_receiver", "creation_datetime")
    search_fields = ("class_receiver", "creation_datetime")


# Register your models here.


admin.site.register(Account, AccountAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(MessageType)
admin.site.register(TeacherStatus)
admin.site.register(Task, TaskAdmin)

admin.site.unregister(Group)
