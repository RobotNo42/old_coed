from django.urls import path
from app02 import views

urlpatterns = [
    path('index/', views.login)

    ]