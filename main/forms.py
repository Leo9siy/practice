from django import forms
from django.forms import Field

from main.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            }
        ),
    )

    class Meta:
        model = Task
        fields = "__all__"
