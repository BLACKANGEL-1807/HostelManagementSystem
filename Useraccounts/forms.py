from django import forms
from django.forms.widgets import PasswordInput


class user_login_form(forms.Form):
   Username         = forms.IntegerField()
   Password         = forms.CharField(max_length=20,widget=PasswordInput())  
   Email_ID         = forms.EmailField()
