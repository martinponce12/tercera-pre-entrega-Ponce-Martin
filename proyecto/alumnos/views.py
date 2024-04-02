from django.shortcuts import render
from alumnos.models import Alumno
from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return render( request , "plantilla.html")



def alta_alumno(request,nombre):
    alumno = Alumno(nombre=nombre, camada=1010)
    alumno.save()
    texto = f"Se guardo en la BD el alumno: {alumno.nombre}{alumno.camada}"
    return HttpResponse(texto)