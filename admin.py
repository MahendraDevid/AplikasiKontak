from django.contrib import admin
from .models import sekolah

class SekolahAdmin(admin.ModelAdmin):
    list_display = ['nama', 'email', 'alamat', ]

admin.site.register(sekolah, SekolahAdmin)