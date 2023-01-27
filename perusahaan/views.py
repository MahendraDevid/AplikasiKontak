from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Perusahaan


def index(request):
    perusahaan_list = Perusahaan.objects.all()
    template = 'perusahaan/perusahaan.html'
    context = {
        'perusahaan': perusahaan_list
    }
    return render(request, template, context)