from django import forms
from .models import HiringInfo, Jobpost


class HiringForm(forms.ModelForm):

    class Meta():
        
        model = HiringInfo

        fields = '__all__'

class PostJobForm(forms.ModelForm):

    class Meta():

        model = Jobpost
        fields = '__all__'