from django.urls import path, include
from .views import *

urlpatterns = [
    path('', bienvenidos, name= "bienvenidos"),
    path('inicio/', bienvenidos, name= "bienvenidos"),
    path('profesionales/', profesionales, name="profesionales"),
    path('estudios/', estudios, name="estudios"),
    path('preguntasfrecuentes/', preguntasfrecuentes, name="preguntasfrecuentes"),
    path('contactanos/', contactanos, name="contactanos"),
    
   path('profesionalesform/', profesionalesform, name="profesionalesform"),
   
   path('buscarprofesionales/', buscarProfesional, name="buscarprofesional"),
   path('buscar/', buscar),
   
]