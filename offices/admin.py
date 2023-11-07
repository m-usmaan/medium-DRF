from django.contrib import admin

from offices.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_filter = ('title', 'slug')
    list_display = ('title', 'slug')

class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'department')
    list_display = ('name', 'email', 'department')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)