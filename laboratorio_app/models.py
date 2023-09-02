from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profesionales(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email = models.EmailField()
    matricula = models.IntegerField()
    m_especializacion = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Profesional: {self.apellido} , {self.nombre}"
    
    class Meta:
         verbose_name = "Profesional"
         verbose_name_plural = "Profesionales"
    
class PreguntasFrecuentes(models.Model):
    pregunta =  models.CharField(max_length=200)
    respuesta = models.CharField(max_length=500)
      
    class Meta:
        verbose_name = "Q&A"
        verbose_name_plural = "Preguntas frecuentes"
          
class Estudios(models.Model):
    prestacion = models.CharField(max_length=800)
    valor = models.IntegerField(null=1)
    
    class Meta:
         verbose_name = "Estudio"
         verbose_name_plural = "Estudios"
 
class Paciente(models.Model):
    nombre = models.CharField(max_length=200)  
    apellido = models.CharField(max_length=200)
    email =   models.EmailField()
    documento = models.IntegerField()
    telefono = models.IntegerField()
    
class Contactos(models.Model):
    telefonos = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    horarios = models.CharField(max_length=50)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"