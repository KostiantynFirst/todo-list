from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "content",
            "is_done",
            "deadline",
            "tags",
        )
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }
