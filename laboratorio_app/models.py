from django.db import models

# Create your models here.

class Profesionales(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email = models.EmailField()
    matricula = models.CharField(max_length=50)
    id_especializacion = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Especializacion(models.Model):
    especialización = models.CharField(max_length=100)
      
    class Meta:
         verbose_name = "Especialización"
         verbose_name_plural = "Especializaciones"
          
class Estudios(models.Model):
    estudios = models.CharField(max_length=100)
    estudios_corto = models.CharField(max_length=5)
 
class Preguntasfrecuentes(models.Model):
    preguntas = models.CharField(max_length=200)  
    repuestas = models.CharField(max_length=200)       
                              

class Contactos(models.Model):
    telefonos = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    horarios = models.CharField(max_length=50)