from django.contrib import admin
from centres.models import Centres,Employee

# Register your models here.

class CentresAdmin(admin.ModelAdmin):
   list_display = [field.name for field in Centres._meta.get_fields()]

class EmployeeAdmin(admin.ModelAdmin):
   list_display = [field.name for field in Employee._meta.get_fields()]


admin.site.register(Centres,CentresAdmin)
admin.site.register(Employee,EmployeeAdmin)
