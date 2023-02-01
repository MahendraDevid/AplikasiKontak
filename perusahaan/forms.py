from django import forms
from .models import Perusahaan

class PerusahaanForm(forms.ModelForm):
   class Meta:
       model = Perusahaan
       fields = ['nama_perusahaan', 
                 'kategori',
                 'bidang',
                 'daerah',
                 'nama_pic',
                 'jabatan', 
                 'hp',
                 'email',
                 'kabupaten_kota',
                 'kecamatan',]
