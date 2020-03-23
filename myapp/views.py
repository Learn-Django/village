from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

def kepala_keluarga(request):
    return render(request,'myapp/kepala_keluarga.html')

def opsi_pekerjaan(request):
    return render(request,'myapp/opsi_pekerjaan.html')

def opsi_pendidikan(request):
    return render(request,'myapp/opsi_pendidikan.html')

def pengguna(request):
    return render(request,'myapp/pengguna.html')

def pengaturan_umum(request):
    return render(request,'myapp/pengaturan_umum.html')