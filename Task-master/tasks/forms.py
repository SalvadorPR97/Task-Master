from django import forms
from . import models

class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar", required=False)
    priority = forms.MultipleChoiceField(
        label="Prioridad",
        choices=[
            ('L', 'Baja'),
            ('N', 'Normal'),
            ('H', 'Alta')
        ],
        widget=forms.CheckboxSelectMultiple(),
        initial=['H', 'N'],
        required=False
    )

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = [
            'name',
            'code',
            'description',
            'start_date',
            'end_date',
        ]

class TasksForm(forms.Form):
    tasks = forms.CharField(
        label= 'Tareas nuevas',
        widget=forms.Textarea(),
        )

        