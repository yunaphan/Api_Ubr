from django.urls import path
from . import views

urlpatterns = [
    path('ListSpecies/', views.getTenCX, name="Get List Tree Name")
]
