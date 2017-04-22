from django import forms

class IniciarSesionForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	contrasena_form = forms.CharField(max_length = 20)

class RegistrarProveedorForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	telefono_form = forms.IntegerField()
	direccion_form = forms.CharField()
	email_form = forms.EmailField()
