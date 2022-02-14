from django.db import models

# Create your models here.
class Contact(models.Model):
    isim =  models.CharField(verbose_name="İsim*", max_length=255,default="", blank=False)
    eposta = models.EmailField(verbose_name="E-posta Adresi*",default="", blank=False)
    degisim = models.CharField(verbose_name="Değiştirilecek/Eklenecek Terim/Kısaltma*", max_length=255, default="",blank=False)
    problem = models.CharField(verbose_name="Problem Tanımı(Opsiyonel)", max_length=600,default="", blank=True)
    oneri= models.CharField(verbose_name="Önerilen Değişiklik/Ekleme(Opsiyonel)",max_length=600,default="", blank=True)

    def __str__(self):
        return self.degisim
