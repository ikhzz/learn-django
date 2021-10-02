from market.models import Product
from django.shortcuts import redirect, render
from market.forms import CreateProductForm, CreateTransactionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Accounts

def checkSuplier(param):
  return param.role == 'suplier'

def checkCostumer(param):
  return param.role == 'costumer'

# Create your views here.
def index(request):
  data = Product.objects.all()
  return render(request, 'market/index.html', {'data': data})

@login_required(login_url='/user/signin/')
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

@login_required(login_url='/user/signin/')
@user_passes_test(checkCostumer,login_url='/home/')
def buy(request, id):
  get = Product.objects.get(id=id)

  if request.user.pk == get.suplier.pk:
    return redirect('market:index')

  if request.method == 'POST':
    trans = CreateTransactionForm(request.POST)
    if trans.is_valid():
      data = trans.save(commit=False)
      data.total = request.POST['total']
      data.product_id = get
      data.costumer_id = request.user
      get.stock = get.stock - int(request.POST['amount'])
      get.save()
      data.save()
      return redirect('market:index')
    else:
      form = CreateTransactionForm(request.POST)
  else:
    form = CreateTransactionForm()
  
  return render(request, 'market/transaction.html',{'form': form,'data': get})

def addStock(request, id):
  get = Product.objects.get(id=id)
  form = CreateProductForm()
  if request.user.pk != get.suplier.pk:
    return redirect('market:index')

  if request.method == 'POST':
    get.name = request.POST['name']
    get.price = request.POST['price']
    get.stock = request.POST['stock']
    get.save()
    return redirect('market:index')
  
  return render(request, 'market/addStock.html', {'form': form, 'get':get})