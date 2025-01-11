from django import forms
from .models import Application
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'age', 'address', 'cet_marks', 'aadhar_card', 'cet_marksheet']
