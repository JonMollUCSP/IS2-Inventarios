from django import forms

class IniciarSesionForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	contrasena_form = forms.CharField(max_length = 20)

class RegistrarProductoForm(forms.Form):
        nombre_form = forms.CharField(max_length = 20)
        tipo_form =  forms.CharField(max_length = 20)
        valor_form = forms.IntegerField()
