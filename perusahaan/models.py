from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class KategoriPerusahaan(models.TextChoices):
    SWASTA = 'Swasta', _('Swasta')
    PEMERINTAHAN= 'Pemerintahan', _('Pemerintahan')

# Create your models here.
class Perusahaan(models.Model):
    nama_perusahaan = models.CharField(max_length=30)
    kategori = models.CharField(
        max_length=20,
        choices=KategoriPerusahaan.choices,
    )

    bidang = models.CharField(max_length=50)
    daerah = models.CharField(blank=True, null=True, max_length=50)
    nama_pic = models.CharField(blank=True, null=True, max_length=50)
    jabatan = models.CharField(blank=True, null=True, max_length=50)
    hp = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
   
 
    kabupaten_kota = models.CharField(blank=True, null=True, max_length=50)
    kecamatan = models.CharField(blank=True, null=True, max_length=50)
   
    # default
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="Perusahaan_created_by")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        db_table = "Perusahaan"
        ordering = ["-id"]
        verbose_name_plural = "Perusahaan"


    
