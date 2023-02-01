from django.test import TestCase
from .models import Siswa
from django.core.exceptions import ObjectDoesNotExist


class SiswaTestCase(TestCase):
    def setUp(self):
        Siswa.objects.create(nama = "Devid", email = "test@gmail.com", hp = 1)
    
    def test_Siswa_cek_nama(self):
        """ Cek nama Siswa """
        test = Siswa.objects.get(nama = "Devid")
        self.assertEqual(test.nama, "Devid")

    def test_update(self):
        instance = Siswa(nama = "Devid", email = "test@gmail.com", hp =1)
        instance.save()
        
        instance.nama = "Devid"
        instance.save()

        updated_instance = Siswa.objects.get(id=instance.id)

        self.assertEqual(updated_instance.nama, "Devid")

    def test_read(self):
        
        instance = Siswa(nama = "Devid",)
        instance.save()
        
        retrieved_instance = Siswa.objects.get(id=instance.id)

        self.assertEqual(retrieved_instance.nama, 'Devid')

    def test_delete(self):
        
        instance = Siswa(nama = "Devid",)
        instance.save()

        
        instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Siswa.objects.get(id=instance.id)

    

    

        
