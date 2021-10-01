from django.db import models
from accounts.models import Accounts

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.PositiveIntegerField()
  stock = models.PositiveSmallIntegerField()
  image = models.ImageField()
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  suplier = models.ForeignKey(Accounts, on_delete=models.SET_DEFAULT, default=None)

class Transaction(models.Model):
  amount = models.PositiveSmallIntegerField()
  total = models.PositiveIntegerField()
  createdAt = models.DateTimeField(auto_now_add=True)
  product_id = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=None)
  costumer_id = models.ForeignKey(Accounts, on_delete=models.SET_DEFAULT, default=None)