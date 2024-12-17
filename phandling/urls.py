from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.project_dashboard, name='project_dashboard'),
]