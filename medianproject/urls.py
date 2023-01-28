from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sekolah/", include("sekolah.urls"), name='sekolah'),
    path("siswa/", include("siswa.urls"), ),
    path("perusahaan/", include("perusahaan.urls"), name='perusahaan'),
    
    path('', views.index),

]
