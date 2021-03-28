from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

from .models import Subject
from .models import PracticeTask, TheoryTask
from .forms import TheoryTaskForm

# Create your views here.


class TheoryTaskCreateView(CreateView):
    template_name = "eduspace/taskcreate.html"
    form_class = TheoryTaskForm
    success_url = "/eduspace/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context


def index(req):
    template = loader.get_template("eduspace/index.html")
    subjects = Subject.objects.all()
    contex = {"subs": subjects}
    return HttpResponse(template.render(contex, req))


def subject(req, subj_id):
    subjects = Subject.objects.all()
    current_subject = Subject.objects.get(pk=subj_id)
    # tasks = PracticeTask.objects.get(subject=subj_id) + TheoryTask.objects.get(subject=subj_id)
    context = {"subs": subjects, "sel_sub": current_subject}
    return render(req, 'eduspace/subject.html', context)
