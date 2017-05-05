from django import forms

class IniciarSesionForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	contrasena_form = forms.CharField(max_length = 20)

class RegistrarProductoForm(forms.Form):
        nombre_form = forms.CharField(max_length = 20)
        tipo_form =  forms.CharField(max_length = 20)
        valor_form = forms.IntegerField()

class RegistrarProveedorForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	telefono_form = forms.IntegerField()
	direccion_form = forms.CharField()
	email_form = forms.EmailField()

class RegistrarUsuarioForm(forms.Form):
	nombre_form=forms.CharField(max_length=20)
	contrasena_form=forms.CharField(max_length=20)
	email_form=forms.EmailField()

class PedidoForm(forms.Form):
	fechaRealizada_form = forms.DateField(input_formats='%Y/%m/%d')