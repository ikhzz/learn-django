from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from accounts.forms import SigninForm

# Create your views here.
def signupView(request):
  return render(request, 'accounts/signup.html')

def signinView(request):

  # if request.method == 'POST':

  #   print('login try')
  # else:
  #   form = SigninForm()
  form = SigninForm()
  return render(request, 'accounts/signin.html', context={'form': form})

def signoutView(request):
  logout(request)
  return redirect('market:index')