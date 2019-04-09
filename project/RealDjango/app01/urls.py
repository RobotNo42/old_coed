from django.urls import path
from app01 import views

urlpatterns = [
    path('index/', views.Login.as_view()),
    path('love/', views.love),
    path('jingdong/', views.jingdong),
    path('jd_index/', views.jd_index)

    ]