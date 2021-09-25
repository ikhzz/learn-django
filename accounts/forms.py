from django.forms import ModelForm
from django import forms
from accounts.models import Accounts

class SigninForm(ModelForm):
  class Meta:
    model = Accounts
    fields = ['email', 'password']
