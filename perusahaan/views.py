from django.shortcuts import render,redirect

from .forms import PerusahaanForm
from .models import Perusahaan

def update(request, id):
    perusahaan_update = Perusahaan.objects.get(id=id)
    
    data = {
        'nama_perusahaan':  perusahaan_update.nama_perusahaan,
        'kategori': perusahaan_update.kategori,
        'bidang': perusahaan_update.bidang,
        'daerah': perusahaan_update.daerah,
        'nama_pic': perusahaan_update.nama_pic, 
        'jabatan': perusahaan_update.jabatan,
        'hp': perusahaan_update.hp,
        'email': perusahaan_update.email,
        'kabupaten_kota' : perusahaan_update.kabupaten_kota,
        'kecamatan' : perusahaan_update.kecamatan,
    }   
    
    perusahaan_form = PerusahaanForm(request.POST or None, initial=data, instance=perusahaan_update)
    
    if request.method == 'POST':
        if perusahaan_form.is_valid():
            perusahaan_form.save()
            
        return redirect('perusahaan:list')
    
    context = {
        "perusahaan_form": perusahaan_form,
    }
            
    return render(request, 'perusahaan/create.html', context)


def delete(request, id):
    Perusahaan.objects.get(pk=id).delete()
    return redirect('perusahaan:list')

def create(request):
    perusahaan_form = PerusahaanForm(request.POST or None)
    
    if request.method == 'POST':
        if perusahaan_form.is_valid():
            perusahaan_form.save()
            
        return redirect('perusahaan:list')
    
    context = {
        "perusahaan_form": perusahaan_form,
    }
            
    return render(request, 'perusahaan/create.html', context)

def list(request):
    perusahaan_list = Perusahaan.objects.all()
    return render(request, 'perusahaan/perusahaan.html', {'perusahaan_list': perusahaan_list})


