from django.contrib import admin
from .models import Perusahaan

class PerusahaanAdmin(admin.ModelAdmin):
    list_display = ['nama_perusahaan', 'email', 'hp', ]

admin.site.register(Perusahaan, PerusahaanAdmin)