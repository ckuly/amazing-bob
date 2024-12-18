from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .forms import ProjectForm
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def releases(request):
    return render(request, 'releases.html')


def user_projects(request, pk=None):
    if pk:
        # Fetch the specific project by primary key
        project = get_object_or_404(Project, pk=pk)
        context = {
            'project': project,
        }
        template = 'user/project_detail.html'  # Use a dedicated template for the detailed view
    else:
        # Fetch all projects for the user_projects view
        projects = Project.objects.all()
        context = {
            'projects': projects,
        }
        template = 'user/projects.html'  # Use the existing template for the list view

    return render(request, template, context)

def project_dashboard(request):
    projects = Project.objects.all()  # Retrieve all projects
    return render(request, 'project_dashboard.html', {'projects': projects})

def register(request):
    form = UserCreationForm()
    return render(request, 'registration/login.html', {"form": form})

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.manager = request.user  # Associate the project with the logged-in user
            project.save()
            return redirect('user_projects')
    else:
        form = ProjectForm()

    return render(request, 'user/project_create.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            project.delete()
            messages.success(request, f'Project "{project.title}" deleted successfully.')
            return redirect('user_projects')
    return render(request, 'user/project_delete.html', {'project': project})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('user_projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'user/project_edit.html', {'form': form})