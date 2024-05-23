from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class BackForm(forms.ModelForm):
    class Meta:
        model = Modal
        fields = ('name', 'email', 'number', 'year')


class TestForm(forms.ModelForm):
    class Meta:
        model = Oplata
        fields = ('name', 'number', 'data', 'ccv')


class Register(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ServiceAppointmentForm(forms.ModelForm):
    class Meta:
        model = ServiceAppointment
        fields = ['name', 'phone', 'email', 'service', 'date', 'time']
