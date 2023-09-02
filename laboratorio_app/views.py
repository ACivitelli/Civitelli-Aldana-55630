from .forms import Pacientesform,Preguntasforms,Prestacionesform,Profesionalesform,UserEditform,AvatarFormulario,User,RegistroUsuariosForm
from .models import Avatar,Estudios,Paciente,PreguntasFrecuentes,Profesionales,User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def bienvenidos(request):
    return render(request,"laboratorio_app/bienvenidos.html")

@login_required
def profesionales(request):
    staff_profesionales = {'profesionales': Profesionales.objects.all()}
    return render(request,"laboratorio_app/profesionales.html", staff_profesionales)

def estudios(request):
    prestaciones = {'prestaciones': Estudios.objects.all()}
    return render(request, "laboratorio_app/estudios.html", prestaciones) 

@login_required
def paciente(request):
    datos_pacientes = {'pacientes': Paciente.objects.all()}
    return render(request, "laboratorio_app/paciente.html", datos_pacientes) 


def preguntasfrecuentes(request):
    preguntas = {'preguntas': PreguntasFrecuentes.objects.all()}
    return render(request, "laboratorio_app/preguntasfrecuentes.html", preguntas) 

def contactanos(request):
    return render(request,"laboratorio_app/contactanos.html")

@login_required
def acercademi(request):
    return render(request,"laboratorio_app/acercademi.html")

# --------------------------------------------------------------
#Busqueda del profesionales por especializacion.
# --------------------------------------------------------------

@login_required
def buscarprofesional(request):
    return render(request,"laboratorio_app/buscarprofesional.html")

@login_required
def buscar(request):
    if request.GET['especializacion']:
        busqueda = request.GET['especializacion']
        mprofesionales = Profesionales.objects.filter(m_especializacion= busqueda)
        staff_profesionales = {"profesionales": mprofesionales, 'titulo': f'Lista de médicos especialistas en {busqueda}'}
        
        return render (request, "laboratorio_app/profesionales.html", staff_profesionales)
    return HttpResponse("No se ingresó nada a buscar")

# --------------------------------------------------------------
#Busqueda del paciente por documento.
# --------------------------------------------------------------

@login_required
def buscarpaciente(request):
    return render(request,"laboratorio_app/buscarpaciente.html")

@login_required
def buscarp(request):
    
    if request.GET['documento']:
        busqueda = request.GET['documento']
        dpaciente = Paciente.objects.filter(documento= busqueda)
        dato_paciente = {"pacientes": dpaciente, 'titulo': f'Lista de médicos especialistas en {busqueda}'}
        
        return render (request, "laboratorio_app/paciente.html", dato_paciente)
    return HttpResponse("No se ingresó nada a buscar")


# --------------------------------------------------------------
#Ingreso de datos, modificación y eliminacion de profesionales.
# --------------------------------------------------------------

@login_required
def medicos(request):
     ctx = {'medicos': Profesionales.objects.all()}
     return render(request, "laboratorio_app/profesionales.html", ctx)
 
@login_required  
def updateMedicos(request, id_medico):
    profesionales = Profesionales.objects.get(id = id_medico)
    if request.method == "POST":
        miForm = Profesionalesform(request.POST)
        if miForm.is_valid():
            profesionales.nombre = miForm.cleaned_data.get('nombre')
            profesionales.apellido = miForm.cleaned_data.get('apellido')
            profesionales.email = miForm.cleaned_data.get('email')
            profesionales.matricula = miForm.cleaned_data.get('matricula')
            profesionales.m_especializacion = miForm.cleaned_data.get('m_especializacion')
            profesionales.save()
            return redirect (reverse_lazy ('profesionales'))  

    else:
        miForm = Profesionalesform(initial= {
            'nombre' :  profesionales.nombre,
            'apellido' :  profesionales.apellido,
            'email' : profesionales.email,
            'matricula' : profesionales.matricula,
            'm_especializacion' : profesionales.m_especializacion
            })

    return render(request,"laboratorio_app/profesionales_upgrade.html", {"form": miForm, 'mensaje': "Se modificaron los datos correctamente"})

@login_required
def profesionalesform(request):
    if request.method == "POST":
        miForm = Profesionalesform(request.POST)
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
            return redirect (reverse_lazy ('profesionales')) 
            return render(request, "laboratorio_app/base.html", {'mensaje': f'El médico {profesional_apellido} fué cargado con éxito'})
                  
    else:
        miForm = Profesionalesform()

    return render(request,"laboratorio_app/profesionalesform.html", {"form": miForm})    

@login_required
def deleteprofesional(request, id_medico):
    profesionales = Profesionales.objects.get(id = id_medico)
    profesionales.delete()
    return redirect (reverse_lazy ('profesionales')) 

# --------------------------------------------------------------
#Ingreso de datos, modificación y eliminacion de pacientes.
# --------------------------------------------------------------

@login_required
def pacientes(request):
     ctx = {'pacientes': Paciente.objects.all()}
     return render(request, "laboratorio_app/pacientes.html", ctx)
 
@login_required  
def updatePaciente(request, id_paciente):
    paciente = Paciente.objects.get(id = id_paciente)
    if request.method == "POST":
        miForm = Pacientesform(request.POST)
        if miForm.is_valid():
            paciente.nombre = miForm.cleaned_data.get('nombre')
            paciente.apellido = miForm.cleaned_data.get('apellido')
            paciente.email = miForm.cleaned_data.get('email')
            paciente.documento = miForm.cleaned_data.get('documento')
            paciente.telefono = miForm.cleaned_data.get('telefono')
            paciente.save()
            return redirect (reverse_lazy ('pacientes'))  

    else:
        miForm = Pacientesform(initial= {
            'nombre' :  paciente.nombre,
            'apellido' :  paciente.apellido,
            'email' : paciente.email,
            'documento' : paciente.documento,
            'telefono' : paciente.telefono
            })

    return render(request,"laboratorio_app/paciente_upgrade.html", {"form": miForm, 'mensaje': "Se modificaron los datos correctamente"})

@login_required
def pacientesform(request):
    if request.method == "POST":
        miForm = Pacientesform(request.POST)
        if miForm.is_valid():
            paciente_nombre = miForm.cleaned_data.get('nombre')
            paciente_apellido = miForm.cleaned_data.get('apellido')
            paciente_email = miForm.cleaned_data.get('email')
            paciente_documento = miForm.cleaned_data.get('documento')
            paciente_telefono = miForm.cleaned_data.get('telefono')
            paciente = Paciente(nombre = paciente_nombre,
                                          apellido= paciente_apellido,
                                          email= paciente_email,
                                          documento= paciente_documento,
                                          telefono= paciente_telefono)
            paciente.save()
            return redirect (reverse_lazy ('pacientes')) 
                  
    else:
        miForm = Pacientesform()

    return render(request,"laboratorio_app/pacientesform.html", {"form": miForm})    

@login_required
def deletePaciente(request, id_paciente):
    pacientes = Paciente.objects.get(id = id_paciente)
    pacientes.delete()
    return redirect (reverse_lazy ('pacientes')) 

# --------------------------------------------------------------
#Ingreso de datos, modificación y eliminacion de lista de precios
# --------------------------------------------------------------

def prestaciones(request):
    valor = {'prestaciones': Estudios.objects.all()}
    return render(request, "laboratorio_app/estudios.html", valor)
 
@login_required  
def updatemarcador(request, id_marcador):
    prestacion = Estudios.objects.get(id = id_marcador)
    if request.method == "POST":
        miForm = Prestacionesform(request.POST)
        if miForm.is_valid():
            prestacion.prestacion = miForm.cleaned_data.get('prestacion')
            prestacion.valor = miForm.cleaned_data.get('valor')
            prestacion.save()
            return redirect (reverse_lazy ('estudios'))  

    else:
        miForm = Prestacionesform(initial= {
            'prestacion' :  prestacion.prestacion,
            'valor' :  prestacion.valor,
            })

    return render(request,"laboratorio_app/prestacion_upgrade.html", {"form": miForm, 'mensaje': "Se modificaron los datos correctamente"})

@login_required
def crearmarcador(request):
    if request.method == "POST":
        miForm = Prestacionesform(request.POST)
        if miForm.is_valid():
            p_prestacion = miForm.cleaned_data.get('prestacion')
            p_valor = miForm.cleaned_data.get('valor')
            p = Estudios(prestacion = p_prestacion,
                                valor= p_valor)
            p.save()
            return redirect (reverse_lazy ('estudios'))
                  
    else:
        miForm = Prestacionesform()

    return render(request,"laboratorio_app/prestacionesform.html", {"form": miForm})    

@login_required
def deletemarcador(request, id_marcador):
    prestaciones = Estudios.objects.get(id = id_marcador)
    prestaciones.delete()
    return redirect (reverse_lazy ('estudios')) 

# --------------------------------------------------------------
#Ingreso de datos, modificación y eliminacion de preguntas frecuentes.
# --------------------------------------------------------------

def preguntasfrecuentes(request):
     ctx = {'preguntas': PreguntasFrecuentes.objects.all()}
     return render(request, "laboratorio_app/preguntasfrecuentes.html", ctx)

@login_required  
def updatePregunta(request, id_pregunta):
    pregunta = PreguntasFrecuentes.objects.get(id = id_pregunta)
    if request.method == "POST":
        miForm = Preguntasforms(request.POST)
        if miForm.is_valid():
            pregunta.pregunta = miForm.cleaned_data.get('pregunta')
            pregunta.respuesta = miForm.cleaned_data.get('respuesta')
            pregunta.save()
            return redirect (reverse_lazy ('preguntasfrecuentes'))  

    else:
        miForm = Preguntasforms(initial= {
            'pregunta' :  pregunta.pregunta,
            'respuesta' :  pregunta.respuesta,
            })

    return render(request,"laboratorio_app/preguntas_upgrade.html", {"form": miForm, 'mensaje': "Se modificaron los datos correctamente"})

@login_required
def preguntaform(request):
    if request.method == "POST":
        miForm = Preguntasforms(request.POST)
        if miForm.is_valid():
            p_pregunta = miForm.cleaned_data.get('pregunta')
            p_respuesta = miForm.cleaned_data.get('respuesta')
            pregunta = PreguntasFrecuentes(pregunta = p_pregunta,
                                          respuesta= p_respuesta)
            pregunta.save()
            return redirect (reverse_lazy ('preguntasfrecuentes'))
                  
    else:
        miForm = Preguntasforms()

    return render(request,"laboratorio_app/preguntasform.html", {"form": miForm})    

@login_required
def deletePregunta(request, id_pregunta):
    pregunta = PreguntasFrecuentes.objects.get(id = id_pregunta)
    pregunta.delete()
    return redirect (reverse_lazy ('preguntasfrecuentes')) 

# --------------------------------------------------------------
#Login/Logout/Registro del Administrador
# --------------------------------------------------------------

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username= usuario, password=password)
            if user is not None:
                login(request, user)
                
                try:
                    avatar= Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar=  "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                    
                return render(request, "laboratorio_app/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "laboratorio_app/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        
        else:
            
            return render(request, "laboratorio_app/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
    
    miForm =   AuthenticationForm()  
        
    return render(request, "laboratorio_app/login.html", {"form":miForm})    
            
            
def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "laboratorio_app/base.html", {'mensaje': f'Usuario cargado con éxito'})
    else:
         miForm =  RegistroUsuariosForm()      
            
    return render(request, "laboratorio_app/registro.html", {"form":miForm})  

@login_required  # Asegura que el usuario esté autenticado para acceder a esta vista
def editarperfil(request):
    if request.method == 'POST':
        form = UserEditform(request.POST, instance=request.user)  # Pasar instancia de usuario actual
        print(form)
        if form.is_valid():
            form.save()  # Guardar los cambios en el perfil del usuario
            return render(request,"laboratorio_app/base.html")  # Redirigir a la página de perfil o a donde desees
    else:
        form = UserEditform(instance=request.user)  # Llenar el formulario con los datos del usuario actual
    
    return render(request, "laboratorio_app/editarperfil.html", {'form': form, 'usuario': request.user})


@login_required
def agregaravatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # Borrar avatar anterior
            avatarviejo = Avatar.objects.filter(user=u)
            if len(avatarviejo) > 0:
                for i in range(len(avatarviejo)):
                    avatarviejo[i].delete()

            # Guardar nuevo avatar
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # muestra la imagen 
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"laboratorio_app/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "laboratorio_app/agregaravatar.html", {'form': form })
