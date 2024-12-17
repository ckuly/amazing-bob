from django.contrib import admin
from .models import Project, Client, Employee, Job, Bill


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "start_date", "end_date", "manager"]
    list_filter = ["manager", "start_date", "end_date"]
    list_editable = ["manager"]
    search_fields = ["title", "manager__username"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "company"]
    list_filter = ["company"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "position"]
    list_filter = ["position"]


class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "notes"]
    list_filter = ["title"]


class BillAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_of_issue", "cost"] # __str__ is a placeholder, will change.
    list_filter = ["date_of_issue", "cost"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Bill, BillAdmin)
