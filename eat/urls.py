from django.urls import path
from . import views

urlpatterns = [
    path('', views.dinner, name='eat'),
    path('meal', views.meal, name='meal'),
]
