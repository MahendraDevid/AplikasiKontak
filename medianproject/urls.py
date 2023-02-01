from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomLoginView, HomeView, CustomLogoutView, RegisterView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sekolah/", include("sekolah.urls"), name='sekolah'),
    path("siswa/", include("siswa.urls"), ),
    path("perusahaan/", include("perusahaan.urls"), name='perusahaan'),
    
    path('', views.index, name="home"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

