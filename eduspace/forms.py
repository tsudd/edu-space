from django import forms

from .models import Message
from .models import Task


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("class_receiver", "text", "type")


class TaskForm(forms.ModelForm):
    
    deadline = forms.DateField(
        widget=forms.widgets.SelectDateWidget(
            empty_label=(
                "Choose year",
                "Choose month",
                "Choose day"
            )
        )
    )

    class Meta:
        model = Task
        fields = ('name', "subject", "description", "deadline", "deadline")
