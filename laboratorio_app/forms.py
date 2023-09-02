from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Profesionalesform(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido= forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=False)
    matricula = forms.IntegerField(required=True)
    m_especializacion = forms.CharField(max_length=50, required=True)

class Pacientesform(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido= forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=False)
    documento = forms.IntegerField(required=True)
    telefono = forms.IntegerField(required=True)

class Prestacionesform(forms.Form):
    prestacion = forms.CharField(label="Prestación", max_length=800, required=True)
    valor = forms.IntegerField(required=True)
    
class Preguntasforms(forms.Form):
    pregunta = forms.CharField(label="Pregunta", max_length=200, required=True)
    respuesta= forms.CharField(label="Respuesta", max_length=500, required=True)

class RegistroUsuariosForm(UserCreationForm):  
    email = forms.EmailField(label="Email",required=True )
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2'] 
        
class UserEditform(UserCreationForm):
    email = forms.EmailField(label="Email",required=True )
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)  
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name= forms.CharField(label="Apellido/s", max_length=50, required=False)
    
    class Meta:
        model = User
        fields = ['email','password1', 'password2','first_name', 'last_name'] 

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)    