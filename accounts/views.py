from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from accounts.forms import SigninForm

# Create your views here.
def signupView(request):
  return render(request, 'accounts/signup.html')

def signinView(request):
  
  msg = ''
  if request.method == 'POST':
    user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
    print(user)
    if user is not None:
      login(request, user)
      return redirect('market:index')
    else:
      msg = "email or password is not valid"
  else:
    form = SigninForm()

  return render(request, 'accounts/signin.html', context={'form': form, 'msg': msg})

def signoutView(request):
  logout(request)
  return redirect('market:index')