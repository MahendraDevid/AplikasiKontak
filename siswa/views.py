from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Siswa

def index(request):
    siswa_list = Siswa.objects.all()
    template = 'siswa/siswa.html'
    context = {
        'siswa': siswa_list
    }
    return render(request, template, context)