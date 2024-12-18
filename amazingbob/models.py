from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Project(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    employees = models.ManyToManyField('Employee')
    jobs = models.ForeignKey('Job', on_delete=models.CASCADE)
    bills = models.ForeignKey('Bill', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    company = models.CharField(max_length=255, blank=True, null=True)
    contacts = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    positions = models.ManyToManyField('Position', related_name='employees')  # Employees can have multiple positions

    def __str__(self):
        return f"{self.name} {self.surname}"


class Position(models.Model):
    title = models.CharField(max_length=255)
    salary = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7)  # Optional description of the position
    description = models.TextField(blank=True, null=True)  # Optional description of the position
    responsibilities = models.TextField(blank=True, null=True)  # Optional description of job responsibilities
    requirements = models.TextField(blank=True, null=True)  # Optional requirements for the position

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Bill(models.Model):
    date_of_issue = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bill {self.id}"  # NOQA works as intended
