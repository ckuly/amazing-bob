from django.shortcuts import render
from .models import Project
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'base.html')

def faq(request):
    return render(request, 'faq.html')

def releases(request):
    return render(request, 'releases.html')

def user_projects(request):
    projects = Project.objects.filter(manager=request.user)
    return render(request, 'user/projects.html', {'projects': projects})

def project_dashboard(request):
    projects = Project.objects.all()  # Retrieve all projects
    return render(request, 'project_dashboard.html', {'projects': projects})

def register(request):
    form = UserCreationForm()
    return render(request, 'registration/login.html', {"form": form})
