from django.urls import path
from market import views

app_name = 'market'

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="index"),
    path('create', views.createProduct, name="create")
]