from django.forms import ModelForm

from .models import TheoryTask


class TheoryTaskForm(ModelForm):
    class Meta:
        model = TheoryTask
        fields = ('name', "subject", "description", "creation_date")
