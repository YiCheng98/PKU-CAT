from django.urls import path

from . import views

urlpatterns = [
    path('demo/', views.demo),
    path('index/', views.index),
    path('', views.archive),
]