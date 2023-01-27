from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sekolah

def index(request):
    sekolah_list = Sekolah.objects.all()
    return render(request, 'sekolah/sekolah.html', {'sekolah_list': sekolah_list})