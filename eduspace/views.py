from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework import permissions

from .models import Subject, Student, Teacher, Class, Account
from .models import Message
from .models import Task
from .forms import MessageForm
from .forms import TaskForm

# Create your views here.
from .serializers import AccountSerializer


class MessageCreateView(UserPassesTestMixin, CreateView):
    template_name = "eduspace/messagecreate.html"
    form_class = MessageForm
    success_url = reverse_lazy('eduspace:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Message.objects.all()
        return context

    def test_func(self):
        return self.request.user.is_staff


class TaskCreateView(UserPassesTestMixin, CreateView):
    template_name = "eduspace/taskcreate.html"
    form_class = TaskForm
    success_url = reverse_lazy("eduspace:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ####
        ####
        return context

    def test_func(self):
        return self.request.user.is_staff


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def index(req):
    template = loader.get_template("eduspace/ind.html")
    context = _get_messages_and_subjects(req)
    # for message in messages:
    #     message.__setattr__("teacher", Teacher.objects.get(pk=message.sender))
    return HttpResponse(template.render(context, req))


@login_required
def subject(req, subj_id):
    context = _get_messages_and_subjects(req)
    context["sel_sub"] = Subject.objects.get(pk=subj_id)
    context["tasks"] = list(Task.objects.filter(subject=subj_id))
    return render(req, 'eduspace/subject.html', context)


def _get_messages_and_subjects(req):
    try:
        if req.user.is_staff:
            teacher = Teacher.objects.get(user=req.user)
            subjects = Subject.objects.filter(teacher=teacher.pk)
            classes = [Class.objects.get(curator=teacher.pk)]
            classes.extend(Class.objects.filter(pk__in=(map(lambda sub: sub.stud_class.pk, subjects))))
            messages = Message.objects.filter(class_receiver__in=tuple(classes))
        else:
            student = Student.objects.get(user=req.user)
            subjects = Subject.objects.filter(stud_class=student.stud_class.pk)
            messages = Message.objects.filter(class_receiver=student.stud_class.pk)
    except:
        return {}
    else:
        return {"subs": subjects, "messages": messages}


@login_required
def task(req, task_id):
    context = _get_messages_and_subjects(req)
    context["sel_task"] = Task.objects.get(pk=task_id)
    return render(req, "eduspace/task.html", context)


@login_required
def message_del(req, mes_id):
    Message.objects.filter(pk=mes_id).delete()
    return index(req)
