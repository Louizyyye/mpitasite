from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.patient_register, name="patient_register"),
    path('login/', views.patient_login, name="patient_login"),
]
