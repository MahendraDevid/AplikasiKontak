from django.contrib import admin
from models import siswa

class SiswaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'email', 'hp' ,'alamat', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'nisn']

admin.site.register(siswa, SiswaAdmin)