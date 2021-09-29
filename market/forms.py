from django.forms import ModelForm
from django import forms

from market.models import Product

class CreateProductForm(ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price', 'stock']
