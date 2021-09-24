from django.urls import path
from market import views

app_name = 'market'

urlpatterns = [
    path('', views.index, name="index")
]