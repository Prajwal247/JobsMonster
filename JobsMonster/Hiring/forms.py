from django import forms
from .models import HiringInfo, Jobpost


class DateInput(forms.DateInput):
    input_type = 'date'


class HiringForm(forms.ModelForm):

    class Meta():
        
        model = HiringInfo

        fields = '__all__'
        widgets = {
            'date':DateInput()
        }
class PostJobForm(forms.ModelForm):

    class Meta():

        model = Jobpost
        fields = ['title','description','date','category','estimated_time']
        widgets = {
            'date':DateInput()
        }