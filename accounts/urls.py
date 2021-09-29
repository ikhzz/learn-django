from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signupView, name="signup"),
    path('signin/', views.signinView, name="signin"),
    path('signout', views.signoutView, name="signout")
]