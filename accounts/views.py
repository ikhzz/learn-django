from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from accounts.forms import SigninForm, SignupForm
from accounts.models import Accounts

# Create your views here.
def signupView(request):
  
  if request.method == "POST":
    form = SignupForm(data=request.POST)

    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(request.POST['password'])
      user.save()
      return redirect('market:index')
    
  else:
    form = SignupForm()

  return render(request, 'accounts/signup.html', context={'form': form})

def signinView(request):
  form = SigninForm()
  msg = ''

  if request.method == 'POST':
    # if needed check user email before
    # checkUser = Accounts.objects.get(email__exact=request.POST['email'])
    user = authenticate(request, email=request.POST['email'], password=request.POST['password'])

    if user is not None:
      login(request, user)
      return redirect('market:index')
    else:
      msg = "email or password is not valid"

  return render(request, 'accounts/signin.html', context={'form': form, 'msg': msg})

def signoutView(request):
  logout(request)
  return redirect('market:index')