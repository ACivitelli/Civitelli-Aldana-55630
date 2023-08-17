from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def bienvenidos(request):
    return render(request,"laboratorio_app/bienvenidos.html")

def profesionales(request):
    staff_profesionales = {'profesionales': Profesionales.objects.all()}
    print (staff_profesionales)  
    return render(request,"laboratorio_app/profesionales.html", staff_profesionales)

def estudios(request):
    informes = {'estudios': Estudios.objects.all()}
    return render(request,"laboratorio_app/estudios.html",informes)

def preguntasfrecuentes(request):
    # consultas = {'consultas': Profesionales.objects.all()}
    return render(request,"laboratorio_app/preguntasfrecuentes.html")

def contactanos(request):
    # contactos = {'contactos': Profesionales.objects.all()}
    return render(request,"laboratorio_app/contactanos.html")

def profesionalesform(request):
    if request.method == "POST":
        miForm = Profesionalesform(request.POST)
        print(miForm)
        if miForm.is_valid():
            profesional_nombre = miForm.cleaned_data.get('nombre')
            profesional_apellido = miForm.cleaned_data.get('apellido')
            profesional_email = miForm.cleaned_data.get('email')
            profesional_matricula = miForm.cleaned_data.get('matricula')
            profesional_m_especializacion = miForm.cleaned_data.get('m_especializacion')
            profesionales = Profesionales(nombre = profesional_nombre,
                                          apellido= profesional_apellido,
                                          email= profesional_email,
                                          matricula= profesional_matricula,
                                          m_especializacion= profesional_m_especializacion)
            profesionales.save()
            return render(request, "laboratorio_app/base.html")
    else:
        miForm = Profesionalesform()

    return render(request,"laboratorio_app/profesionalesform.html", {"form": miForm})

def buscarProfesional(request):
    return render(request,"laboratorio_app/buscarprofesional.html")

def buscar(request):

    if request.get['nombre']:
        nombre = request.get['nombre']
        datos_profesionales = Profesionales.objects.filter(nombre__icontains=nombre)
        staff_profesionales = {
            'nombre': nombre,
            'datos_profesionales':datos_profesionales
            }
        return (request, "laboratorio_app/buscarprofesional.html", staff_profesionales)

    return HttpResponse("No se ingresó nada a buscar")


