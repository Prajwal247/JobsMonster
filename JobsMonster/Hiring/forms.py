from django import forms
from .models import HiringInfo


class HiringForm(forms.ModelForm):

    class Meta():
        
        model = HiringInfo

        fields = '__all__'