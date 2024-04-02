from django.shortcuts import render
from profesores.models import Profesor
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render( request , "plantilla.html")




def alta_profesor(request,nombre):
    profesor = Profesor(nombre=nombre, camada=1212 )
    profesor.save()
    texto = f"Se guardo en la BD el profesor: {profesor.nombre} {profesor.camada}"
    return HttpResponse(texto)