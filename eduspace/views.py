from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Subject
from .models import Message
from .models import PracticeTask, TheoryTask
from .forms import TheoryTaskForm
from .forms import MessageForm

# Create your views here.


class MessageCreateView(CreateView):
    template_name = "eduspace/messagecreate.html"
    form_class = MessageForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Message.objects.all()
        return context


class TheoryTaskCreateView(CreateView):
    template_name = "eduspace/taskcreate.html"
    form_class = TheoryTaskForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context


@login_required
def index(req):
    template = loader.get_template("eduspace/index.html")
    subjects = Subject.objects.all()
    contex = {"subs": subjects}
    return HttpResponse(template.render(contex, req))


@login_required
def subject(req, subj_id):
    subjects = Subject.objects.all()
    current_subject = Subject.objects.get(pk=subj_id)
    # tasks = PracticeTask.objects.get(subject=subj_id) + TheoryTask.objects.get(subject=subj_id)
    context = {"subs": subjects, "sel_sub": current_subject}
    return render(req, 'eduspace/subject.html', context)
