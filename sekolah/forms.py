from django import forms
from .models import Sekolah

class SekolahForm(forms.ModelForm):
   class Meta:
       model = Sekolah
       fields = ['npsn', 
                 'nama',
                 'email',
                 'hp',
                 'alamat',
                 'provinsi', 
                 'kabupaten_kota',
                 'kecamatan',
                 'status',]
