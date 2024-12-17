from django.shortcuts import render
from .models import Project

def project_dashboard(request):
    projects = Project.objects.prefetch_related('employees').select_related('jobs', 'bills', 'client', 'manager') # NOQA
    context = {
        'projects': projects
    }
    return render(request, 'project_dashboard.html', context)