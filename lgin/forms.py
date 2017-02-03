from django import forms
from django.utils.safestring import mark_safe
from django.template import Template



class LoginForm(forms.Form):
    usr = forms.CharField(label='Username:', max_length=10)
    pwd = forms.CharField(label=mark_safe('<br>Password:'), max_length=10,widget=forms.PasswordInput)
    keep_logged = forms.BooleanField(required=False, label=mark_safe('<br><br>Keep me logged in '))

    buttons = Template("""
        <button class="waves-effect waves-teal btn-flat">Register</button>
        <button class="waves-effect waves-light btn" type="submit">Login</button>
    """)
