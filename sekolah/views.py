from django.shortcuts import render,redirect

from .forms import SekolahForm
from .models import Sekolah

def update(request,id):
    sekolah_update = Sekolah.objects.get(pk=id)
    
    data = {
        'npsn' : sekolah_update.npsn,
        'nama':  sekolah_update.nama,
        'email': sekolah_update.email,
        'hp': sekolah_update.hp,
        'alamat': sekolah_update.alamat,
        'provinsi': sekolah_update.provinsi, 
        'kabupaten_kota': sekolah_update.kabupaten_kota,
        'kecamatan': sekolah_update.kecamatan,
        'status': sekolah_update.status,
    }
    
    sekolah_form = SekolahForm(request.POST or None, initial=data, instance=sekolah_update)
    
    if request.method == 'POST':
        if sekolah_form.is_valid():
            sekolah_form.save()
            
        return redirect('sekolah:list')
    
    context = {
        "sekolah_form": sekolah_form,
    }
            
    return render(request, 'sekolah/create.html', context)

def delete(request, id):
    Sekolah.objects.get(pk=id).delete()
    return redirect('sekolah:list')

def create(request):
    sekolah_form = SekolahForm(request.POST or None)
    
    if request.method == 'POST':
        if sekolah_form.is_valid():
            sekolah_form.save()
            
        return redirect('sekolah:list')
    
    context = {
        "sekolah_form": sekolah_form,
    }
            
    return render(request, 'sekolah/create.html', context)

def list(request):
    sekolah_list = Sekolah.objects.all()
    return render(request, 'sekolah/sekolah.html', {'sekolah_list': sekolah_list})


