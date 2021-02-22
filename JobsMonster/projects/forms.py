from django import forms
from .models import Project, ProjectManpowers, Update


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project

        fields = ['title','description','duration','estimated_manpowers']
        
class UpdateForm(forms.ModelForm):

    class Meta():
        model = Update
        fields='__all__'