from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    height = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    weight = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    goal_weight = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-input'}))



    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'height', 'weight', 'goal_weight')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
