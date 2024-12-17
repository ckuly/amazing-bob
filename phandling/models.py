from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    employees = models.ManyToManyField('Employee')  # employees can work on multiple projects.
    jobs = models.ForeignKey('Job', on_delete=models.CASCADE)  # each job is tied to a single project.
    bills = models.ForeignKey('Bill', on_delete=models.CASCADE)  # each bill is tied to a single project.

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
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


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
