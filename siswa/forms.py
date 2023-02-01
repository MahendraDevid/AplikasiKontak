from django import forms
from .models import Siswa

class SiswaForm(forms.ModelForm):
   class Meta:
       model = Siswa
       fields = ['nama',
                 'email',
                 'hp',
                 'alamat',
                 'jenis_kelamin', 
                 'tempat_lahir',
                 'tanggal_lahir',
                 'nisn',]
