from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')# this means that for the home page, look for index() in views
]
