from django import forms

class Profesionalesform(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido= forms.CharField(max_length=50, required=True)
    email = forms.EmailField(label="Email", required=False)
    matricula = forms.IntegerField(required=True)
    m_especializacion = forms.CharField(max_length=50, required=True)
 