from django.urls import path
from . import views

urlpatterns = [
    path('buscar/', views.buscar_clima, name='buscar_clima'),
]
