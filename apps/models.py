# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Becarios(models.Model):
    Nocontrol = models.IntegerField()
    Nombrealum = models.CharField(max_length=30)
    Appalum= models.CharField(max_length=30)
    Apmalum=models.CharField(max_length=30)
    Caralum=models.CharField(max_length=30)
    Semalum=models.IntegerField()

    def __unicode__(self):
        return ('%s %s %s %s') % (self.Nocontrol, self.Appalum, self.Apmalum, self.Nombrealum)

class Registro(models.Model):
    nocontrol = models.ForeignKey(Becarios, on_delete=models.CASCADE)
    FecReg = models.DateTimeField(auto_now_add=True)
    FechaReg = models.DateField(default=datetime.now())
    HoraRef = models.TimeField(default=datetime.now())

    def __unicode__(self):
       # t = '%s - %s - %s - %s - %s - %s' % (self.FecReg.year,self.FecReg.month, self.FecReg.day, self.FecReg.hour, self.FecReg.minute)
        return ('%s %s/%s/%s %s:%s') % (self.nocontrol,self.FechaReg.year,self.FechaReg.month, self.FechaReg.day, self.HoraRef.hour, self.HoraRef.minute)

