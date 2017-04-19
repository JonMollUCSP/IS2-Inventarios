from django import forms

class LoginForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	contrasena_form = forms.CharField(max_length = 20)
