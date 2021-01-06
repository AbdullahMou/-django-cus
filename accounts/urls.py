from django.views.generic.base import TemplateView
from django.urls import path 
from django.contrib import admin
from .views import SignupView


urlpatterns = [
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('signup/',SignupView.as_view(),name='signup'),
    ]