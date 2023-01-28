from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SekolahForm
from django.template import loader
from .models import Sekolah
from django.contrib import messages

def index(request):
    sekolah_list = Sekolah.objects.all()
    return render(request, 'sekolah/sekolah.html', {'sekolah_list': sekolah_list})

def create(request):
    return render(request, 'sekolah/create.html', )

def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = SekolahForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = SekolahForm(request.POST)
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('sekolah:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class SekolahForm
        form = SekolahForm()
    # merender template form dengan memparsing data form
    return render(request, 'sekolah/create.html', {'form': form})

