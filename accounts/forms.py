from django.forms import ModelForm
from django import forms
from accounts.models import Accounts

class SigninForm(ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = Accounts
    fields = ['email']

class SignupForm(ModelForm):
  username = forms.CharField(required=False)
  password = forms.CharField(widget=forms.PasswordInput())
  confirm_password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = Accounts
    fields = ['email']
  
  def clean(self):
    cleaned_data = super(SignupForm, self).clean()
    password = cleaned_data.get("password")
    confirmPassword = cleaned_data.get("confirm_password")

    if password != confirmPassword:
      raise forms.ValidationError("Password and confirm password mismatch")

    return cleaned_data