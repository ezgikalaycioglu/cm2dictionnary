from django.db import models

# Create your models here.

class Terms(models.Model):
    tr = models.CharField(max_length=200, null=True, blank=True)
    eng = models.CharField(max_length=200, null=True, blank=True)

    tnm = models.TextField(default="")
    dfn = models.TextField(default="")

    id= models.IntegerField(primary_key=True, default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return 'ID: {0} TR: {1} EN: {2}'.format(self.id, self.tr , self.eng)

class Abr(models.Model):
    abr = models.CharField(max_length=200, null=True, blank=True)
    meaning = models.TextField()

    id= models.IntegerField(primary_key=True, default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return 'ID: {0} ABR: {1} MEANING: {2}'.format(self.id, self.abr , self.meaning)
