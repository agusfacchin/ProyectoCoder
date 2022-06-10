from django.db import models

# Create your models here.
class Restaurante (models.Model): 
    nombre=models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=50)
    fechaApertura=models.DateField() 
    calificacion=models.DecimalField(max_digits=1, decimal_places=0) 

class Empleados (models.Model): 
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fechaIngreso=models.DateField()

class Platos (models.Model): 
    nombre=models.CharField(max_length=30)
    precioArg=models.IntegerField()
    aptoCeliaco=models.BooleanField()
