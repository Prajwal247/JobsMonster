from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, TextInput, NumberInput
from django.contrib.auth.models import User
from .models import User

# this is the form for the user to hire another person
class UserRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(
        label = ('Password'),
        widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'required':'True'
        }),
        help_text = ('your passcode cannot be too similar to your personal information, must be more than 8 character alphanumeric and cannot be totally numeric')
    )

    password2 = forms.CharField(
        label = ('Password Confirmation'),
        widget = forms.PasswordInput(attrs = {
            'class':'form-control',
            'type':'password',
            'required':'True'
        }),
        help_text = ('Enter same passcode as above for Verification')
    )


    class Meta():

        model = User
        fields = ['first_name','last_name','email','mobile','DOB','Nationality','password1','password2']

        widgets = {
            'first_name':TextInput(attrs={
                'class':'form-control',
            }),

            'last_name':TextInput(attrs={
                'class':'form-control',
            }),

            'email':EmailInput(attrs = {
                'class':'form-control',
                'placeholder':'Please Provide the valid email',
                'required':'True',
            })
        }


# this is the form for the professional workers

class ProfessionalUserRegistrationForm(forms.ModelForm):

    
    password1 = forms.CharField(
        label = ('Password'),
        widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'required':'True'
        }),
        help_text = ('your passcode cannot be too similar to your personal information, must be more than 8 character alphanumeric and cannot be totally numeric')
    )

    password2 = forms.CharField(
        label = ('Password Confirmation'),
        widget = forms.PasswordInput(attrs = {
            'class':'form-control',
            'type':'password',
            'required':'True'
        }),
        help_text = ('Enter same passcode as above for Verification')
    )


    class Meta():

        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'mobile',
                  'avatar',
                  'Specialization',
                  'Skills',
                  'location',
                  'Gender',
                  'work_experience',
                  'BioData',
                  'currently_employed',
                  'pay_rate',
                  'password1',
                  'password2',]
        widgets = {
            'first_name':TextInput(attrs={
                'class':'form-control',
            }),

            'last_name':TextInput(attrs={
                'class':'form-control',
            }),

            'email':EmailInput(attrs = {
                'class':'form-control',
                'placeholder':'Please Provide the valid email',
                'required':'True',
            })
        }