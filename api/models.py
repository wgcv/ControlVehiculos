from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Emergencia(models.Model):
	alarma = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	latitud = models.DecimalField(max_digits=9, decimal_places=6)
	longitud = models.DecimalField(max_digits=9, decimal_places=6)

class Unidad(models.Model):
	nombre = models.CharField(max_length=200)
	tipo = models.CharField(max_length=200)
	latitud = models.DecimalField(max_digits=9, decimal_places=6)
	longitud = models.DecimalField(max_digits=9, decimal_places=6)

    