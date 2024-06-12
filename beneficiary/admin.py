from django.contrib import admin
from .models import SlotBook,Certificate

# Register your models here.

class SlotBookAdmin(admin.ModelAdmin):
   list_display = [field.name for field in SlotBook._meta.get_fields()]

class CertificateAdmin(admin.ModelAdmin):
   list_display = [field.name for field in Certificate._meta.get_fields()]


admin.site.register(SlotBook,SlotBookAdmin)
admin.site.register(Certificate,CertificateAdmin)