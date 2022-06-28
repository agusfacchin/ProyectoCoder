from django.shortcuts import render, HttpResponse
from appcoder.models import Restaurante, Empleados, Platos 
from django.http import HttpResponse
from django.http.request import QueryDict
from appcoder.forms import RestauranteFormulario, EmpleadosFormulario, PlatosFormulario

# Create your views here.
def restaurante(request):
      if request.method == 'POST':
            miFormulario = RestauranteFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:  
                  informacion = miFormulario.cleaned_data
                  restaurante = Restaurante (nombre=informacion['restaurante'], ubicacion=informacion['ubicacion'], fechaApertura=informacion['fechaApertura'], calificacion=informacion['calificacion'])  
                  restaurante.save()
                  return render(request, "inicio.html") 
      else: 
        miFormulario= RestauranteFormulario() 
      return render(request, "restaurante.html", {"miFormulario":miFormulario})
 
def empleados(request):
      if request.method == 'POST':
            miFormulario = EmpleadosFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:  
                  informacion = miFormulario.cleaned_data
                  empleados = Empleados (nombre=informacion['empleados'], apellido=informacion['apellido'], fechaIngreso=informacion['fechaIngreso']) 
                  empleados.save()
                  return render(request, "empleados.html") 
      else: 
        miFormulario= RestauranteFormulario() 
      return render(request, "restaurante.html", {"miFormulario":miFormulario})

def platos(request):
      if request.method == 'POST':
            miFormulario = PlatosFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:  
                  informacion = miFormulario.cleaned_data
                  platos = Platos (nombre=informacion['platos'], precioArg=informacion['precioArg'], aptoCeliaco=informacion['aptoCeliaco']) 
                  platos.save()
                  return render(request, "platos.html") 
      else: 
        miFormulario= RestauranteFormulario() 
      return render(request, "platos.html", {"miFormulario":miFormulario})    


def buscar(request):
      if  request.GET["precioArg"]:
            precioArg = request.GET['precioArg'] 
            platos = Platos.objects.filter(precioArg__icontains=precioArg)
            return render(request, "inicio.html", {"platos":platos, "precioArg":precioArg})
      else: 
        respuesta = "No hay datos"

      return HttpResponse("Todo ok")  
