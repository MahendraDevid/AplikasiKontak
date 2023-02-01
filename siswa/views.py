from django.shortcuts import render,redirect

from .forms import SiswaForm
from .models import Siswa

def update(request, id):
     siswa_update = Siswa.objects.get(pk= id)
    
     data = {       
         'nama':  siswa_update.nama,
         'email': siswa_update.email,
         'hp': siswa_update.hp,
         'alamat': siswa_update.alamat,
         'jenis_kelamin': siswa_update.jenis_kelamin, 
         'tempat_lahir': siswa_update.tempat_lahir,
         'tanggal_lahir': siswa_update.tanggal_lahir,
         'nisn': siswa_update.nisn,
     }
    
     siswa_form = SiswaForm(request.POST or None, initial=data, instance=siswa_update)
    
     if request.method == 'POST':
         if siswa_form.is_valid():
             siswa_form.save()
            
         return redirect('siswa:list')
    
     context = {
         "siswa_form": siswa_form,
     }
            
     return render(request, 'siswa/create.html', context)

def delete(request, id):
    Siswa.objects.get(pk=id).delete()
    return redirect('siswa:list')

def create(request):
    siswa_form = SiswaForm(request.POST or None)
    
    if request.method == 'POST':
        if siswa_form.is_valid():
            siswa_form.save()
            
        return redirect('siswa:list')
    
    context = {
        "siswa_form": siswa_form,
    }
            
    return render(request, 'siswa/create.html', context)

def list(request):
    siswa_list = Siswa.objects.all()
    return render(request, 'siswa/siswa.html', {'siswa_list': siswa_list})


