from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', bienvenidos, name= "bienvenidos"),
    path('inicio/', bienvenidos, name= "bienvenidos"),
    path('paciente/', paciente, name="pacientes"),
    path('profesionales/', profesionales, name="profesionales"),
    path('estudios/', estudios, name="estudios"),
    path('preguntasfrecuentes/', preguntasfrecuentes, name="preguntasfrecuentes"),
    path('contactanos/', contactanos, name="contactanos"),
    path('acercademi/', acercademi, name="acercademi"),

    
   #Buscar profesional 
   path('buscarprofesional/', buscarprofesional, name="buscarprofesional"),
   path('buscar/', buscar, name="buscar"),
   
   #Buscar paciente 
   path('buscarpaciente/', buscarpaciente, name="buscarpaciente"),
   path('buscarp/', buscarp, name="buscarp"),   
   
   
   #Ingreso de datos, modificación y borrar carga de profesionales.
   path('updateMedicos/<int:id_medico>/', updateMedicos, name="updateMedicos"),   
   path('profesionalesform/', profesionalesform, name="crearprofesional"),
   path('deleteprofesional/<id_medico>/', deleteprofesional, name="deleteprofesional"),

   #Ingreso de datos, modificación y borrar carga de pacientes.
   path('updatePaciente/<int:id_paciente>/', updatePaciente, name="updatePaciente"),   
   path('pacientesform/', pacientesform, name="crearpaciente"),
   path('deletepaciente/<id_paciente>/', deletePaciente, name="deletePaciente"),
   
   #Ingreso de datos, modificación y borrar carga de lista de precios de prestaciones.
   path('updatemarcador/<id_marcador>/', updatemarcador, name="updatemarcador"),   
   path('prestacionesform/', crearmarcador, name="crearmarcador"),
   path('deletemarcador/<id_marcador>/', deletemarcador, name="deletemarcador"),
   
   #Ingreso de datos, modificación y borrar carga de preguntas frecuentes.
   path('updatePregunta/<int:id_pregunta>/', updatePregunta, name="updatePregunta"),   
   path('preguntasform/', preguntaform, name="crearpregunta"),
   path('deletepregunta/<id_pregunta>/', deletePregunta, name="deletePregunta"),   
      
   #Login,Logout y registro del administrador
   path('login/', login_request, name="login"),
   path('logout/', LogoutView.as_view(template_name="laboratorio_app/logout.html"), name="logout" ),
   path('registro/', register, name="registro"),
   path('editarperfil/', editarperfil, name="editarperfil"),
   path('agregaravatar/', agregaravatar, name="agregaravatar"),
   
   
  
]