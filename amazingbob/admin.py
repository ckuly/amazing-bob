from django.contrib import admin
from .models import Project, Client, Employee, Job, Bill, Position


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'client', 'manager', 'image')
    list_filter = ('start_date', 'end_date')
    list_editable = ["manager"]
    search_fields = ["title", "manager__username"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "company"]
    list_filter = ["company"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]
    list_filter = []


class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "notes"]
    list_filter = ["title"]


class BillAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_of_issue", "cost"] # __str__ is a placeholder, will change.
    list_filter = ["date_of_issue", "cost"]

class PositionAdmin(admin.ModelAdmin):
    list_display = ["title", "salary", "responsibilities"]
    list_filter = ["salary"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Position, PositionAdmin)
