from django.contrib.auth.models import User
from django import forms


class Signupform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(help_text='Required')


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']
