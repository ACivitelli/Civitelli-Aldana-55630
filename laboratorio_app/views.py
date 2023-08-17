from django.http import HttpResponse
from django.shortcuts import render
from .models import Profesionales,Estudios
from .forms import ProfesionalesForm

# Create your views here.
def bienvenidos(request):
    return render(request,"laboratorio_app/bienvenidos.html")

def profesionales(request):
    staff_profesionales = {
        'profesionales': Profesionales.objects.all(), 
        'titulo': 'Listado de profesionales'
    }
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

def profesionalesForm(request):
    if request.method == "POST":
        miForm = ProfesionalesForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            profesional_nombre = miForm.cleaned_data.get('nombre')
            profesional_apellido = miForm.cleaned_data.get('apellido')
            profesional_email = miForm.cleaned_data.get('Email')
            profesional_matricula = miForm.cleaned_data.get('matricula')
            profesional_id_especializacion = miForm.cleaned_data.get('especialización')
            profesionales = Profesionales (
                nombre = profesional_nombre,
                apellido= profesional_apellido,
                email= profesional_email,
                matricula= profesional_matricula,
                id_especializacion= profesional_id_especializacion
            )

            profesionales.save()
            
            return render(request, "laboratorio_app/base.html")
    else:
        miForm = ProfesionalesForm()


    return render(request,"laboratorio_app/profesionalesform.html", {"form": miForm})


def buscarProfesional(request):
    return render(request,"laboratorio_app/buscarprofesional.html")

def buscar(request):

    if request.get['nombre']:

        nombre = request.get['nombre']

        datos_profesionales = Profesionales.objects.filter(
            nombre__icontains=nombre
        )

        staff_profesionales = {
            'nombre': nombre,
            'datos_profesionales':datos_profesionales
        }
        
        return (request, "laboratorio_app/buscarprofesional.html", staff_profesionales)

    return HttpResponse("No se ingresó nada a buscar")


