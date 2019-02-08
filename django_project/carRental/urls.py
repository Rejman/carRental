from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="carRental-home"),
    path('users/', views.users, name="carRental-users"),
]
