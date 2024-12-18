from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('releases/', views.releases, name='releases'),
    path('user_projects/', views.user_projects, name='user_projects'),
    path('projects/', views.project_dashboard, name='project_dashboard'),
]