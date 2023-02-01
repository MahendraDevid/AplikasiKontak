from django.test import TestCase
from .models import Perusahaan
from django.core.exceptions import ObjectDoesNotExist


class PerusahaanTestCase(TestCase):
    def setUp(self):
        Perusahaan.objects.create(nama_perusahaan="DevidCompany", kategori="NEGERI", bidang="web")
    
    def test_Perusahaan_cek_nama(self):
        """ Cek nama Perusahaan """
        test = Perusahaan.objects.get(nama_perusahaan="DevidCompany")
        self.assertEqual(test.nama_perusahaan, "DevidCompany")

    def test_update(self):
        instance = Perusahaan(nama_perusahaan="DevidCompany", kategori  = "NEGERI", bidang = "web")
        instance.save()
        
        instance.nama = "DevidCompany"
        instance.save()

        updated_instance = Perusahaan.objects.get(id=instance.id)

        self.assertEqual(updated_instance.nama_perusahaan, "DevidCompany")

    def test_read(self):
        
        instance = Perusahaan(nama_perusahaan="DevidCompany",)
        instance.save()
        
        retrieved_instance = Perusahaan.objects.get(id=instance.id)

        self.assertEqual(retrieved_instance.nama_perusahaan, 'DevidCompany')

    def test_delete(self):
        
        instance = Perusahaan(nama_perusahaan="DevidCompany",)
        instance.save()

        
        instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Perusahaan.objects.get(id=instance.id)
