from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'market/index.html')

def createProduct(request):
  return render(request, 'market/createProduct.html')