from django import forms
from django.utils.safestring import mark_safe

class NameForm(forms.Form):
    usr = forms.CharField(label='Username:', max_length=100)
    pwd = forms.CharField(label=mark_safe('<br>Password:'), max_length=10,)