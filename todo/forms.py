from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(forms.ModelForm):
    title= forms.CharField(label=False, widget= forms.TextInput(attrs={'placeholder':'Add new task...', 'autocomplete':'off'}))
    completed = forms.BooleanField(label=False, required=False)
    class Meta:
        model=Task
        fields='__all__'