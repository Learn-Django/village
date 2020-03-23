from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kepala_keluarga/', views.kepala_keluarga),
    path('opsi_pekerjaan/', views.opsi_pekerjaan),
    path('opsi_pendidikan/', views.opsi_pendidikan),
    path('pengguna/', views.pengguna),
    path('pengaturan_umum/', views.pengaturan_umum)
    
]