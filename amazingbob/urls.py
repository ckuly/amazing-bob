from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('releases/', views.releases, name='releases'),
    path('user_projects/', views.user_projects, name='user_projects'),
    path('user_projects/<int:pk>', views.user_projects, name='user_projects'),
    path('projects/', views.project_dashboard, name='project_dashboard'),
    path('register/', views.register, name='register'),
    path('project_create/', views.project_create, name='project_create'),
    path('project_delete/<int:pk>/', views.project_delete, name='project_delete'),
    path('project_edit/<int:pk>/', views.project_edit, name='project_edit'),
]