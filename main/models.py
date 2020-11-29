from django.db import models
from django.urls import reverse


# Create your models here.
class mquiz(models.Model):
    qdesc = models.CharField(max_length=2000)
    qop1 = models.CharField(max_length=500)
    qop2 = models.CharField(max_length=500)
    qop3 = models.CharField(max_length=500, null=True, blank=True)
    qop4 = models.CharField(max_length=500, null=True, blank=True)
    qop5 = models.CharField(max_length=500, null=True, blank=True)
    qans = models.IntegerField(null=True)
    qhint = models.CharField(max_length=1000, null=True, blank=True)
    qsol = models.CharField(max_length=2000, null=True, blank=True)
    qimg = models.CharField(max_length=2000, null=True, blank=True)
    qimage = models.ImageField(upload_to='mquiz/', null=True, blank=True)
    qhimg = models.ImageField(upload_to='mquiz/', null=True, blank=True)
    qsimg = models.ImageField(upload_to='mquiz/', null=True, blank=True)

    def get_absolute_url(self):
       '''
       This method provides an absolute_url for each object in the mquiz class
       '''
       return reverse("main:show_question", args=[self.pk])
