from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('doctors/', views.doctors, name='dc'),
    path('directions/', views.directions, name='drc'),
    path('', views.home, name='main'),
    path('doctors/sort/<str:name>/', views.sort, name='s_dc')
]