from django.db.models import fields
from django.db.models.fields import CharField
from django.forms import ModelForm
from django import forms

from market.models import Product, Transaction

class CreateProductForm(ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price', 'stock']

class CreateTransactionForm(ModelForm):
  # total is custom because there is no point to have it manualy
  # total = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
  class Meta:
    model = Transaction
    fields = ['amount']

# class AddStock(ModelForm):
#   class Meta:
#     model = Product
#     fields = ['stock', 'price', ]