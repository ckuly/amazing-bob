from django.shortcuts import render
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

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