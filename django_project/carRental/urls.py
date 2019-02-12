from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="carRental-home"),
    path('<str:mark>', views.home, name="carRental-home"),
    path('<int:car_model_id>/desc/', views.desc, name="desc"),
    path('<int:car_id>/rental/', views.rental, name="rental"),
]
