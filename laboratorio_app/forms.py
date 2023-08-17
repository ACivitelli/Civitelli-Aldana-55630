from django import forms

class ProfesionalesForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido= forms.CharField(max_length=50, required=True)
    email = forms.EmailField(label="Email", required=False)
    matricula = forms.IntegerField(required=True)
    id_especializacion = forms.CharField(max_length=50, required=True)
 