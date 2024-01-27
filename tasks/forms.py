from django import forms
from .models import Task, TaskImages


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',
                  'due_date', 'priority', 'is_complete']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = TaskImages
        fields = ['images']
