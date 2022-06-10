from django import forms

class RestauranteFormulario (forms.Form): 
    nombre=forms.CharField(max_length=30)
    ubicacion=forms.CharField(max_length=50)
    fechaApertura=forms.DateField() 
    calificacion=forms.DecimalField(max_digits=1, decimal_places=0) 

class EmpleadosFormulario (forms.Form): 
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    fechaIngreso=forms.DateField()

class PlatosFormulario (forms.Form): 
    nombre=forms.CharField(max_length=30)
    precioArg=forms.IntegerField()
    aptoCeliaco=forms.BooleanField()
