from market.models import Product
from django.shortcuts import redirect, render
from market.forms import CreateProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Accounts

def checkSuplier(param):
  return param.role == 'suplier'

# Create your views here.
def index(request):
  data = Product.objects.all()
  return render(request, 'market/index.html', {'data': data})

@login_required(login_url='user/signin/')
@user_passes_test(checkSuplier,login_url='home/')
def createProduct(request):

  if request.method == 'POST':
    product = CreateProductForm(data=request.POST)
    if product.is_valid():
      data = product.save(commit=False)
      data.suplier_id = request.user.pk
      data.save()
      return redirect('market:index')
    else:
      form = CreateProductForm(data=request.POST)
  else:
    form = CreateProductForm()

  return render(request, 'market/createProduct.html', {'form': form})