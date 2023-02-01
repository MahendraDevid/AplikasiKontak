from django.test import TestCase
from .models import Sekolah
from django.core.exceptions import ObjectDoesNotExist


class SekolahTestCase(TestCase):
    def setUp(self):
        Sekolah.objects.create(npsn="2026822", nama="SMKN 1 Cimahi", status="Negeri")
    
    def test_sekolah_cek_nama(self):
        """ Cek nama sekolah """
        smkn1 = Sekolah.objects.get(nama="SMKN 1 Cimahi")
        self.assertEqual(smkn1.nama, "SMKN 1 Cimahi")

    def test_update(self):
        instance = Sekolah(nama='SMKN 1 Cimahi', status='negeri')
        instance.save()
        
        instance.nama = 'SMKN 2 Cimahi'
        instance.save()

        updated_instance = Sekolah.objects.get(id=instance.id)

        self.assertEqual(updated_instance.nama, 'SMKN 2 Cimahi')

    def test_read(self):
        
        instance = Sekolah(nama='SMKN 1 Cimahi',)
        instance.save()
        
        retrieved_instance = Sekolah.objects.get(id=instance.id)

        self.assertEqual(retrieved_instance.nama, 'SMKN 1 Cimahi')

    def test_delete(self):
        
        instance = Sekolah(nama='SMKN 1 Cimahi',)
        instance.save()

        
        instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Sekolah.objects.get(id=instance.id)
