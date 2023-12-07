from django import forms

from manager.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        blank=True
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput,
        required=False,
    )
    
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
