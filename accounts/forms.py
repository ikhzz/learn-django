from django.db import models
from django.forms import ModelForm
from django import forms
from accounts.models import Accounts

class SigninForm(ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = Accounts
    fields = ['email', 'password']