from django.forms import ModelForm

from .models import TheoryTask
from .models import Message


class TheoryTaskForm(ModelForm):
    class Meta:
        model = TheoryTask
        fields = ('name', "subject", "description", "creation_date")


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ("class_receiver", "text", "type")
