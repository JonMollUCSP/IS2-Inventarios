from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

<<<<<<< HEAD
from .forms import IniciarSesionForm
from .models import Usuario
=======
from .forms import *
from .models import *
>>>>>>> jonathan

def IniciarSesionView(request):
	formulario = IniciarSesionForm(request.POST or None)
	contexto = { "formulario" : formulario }

	if formulario.is_valid():
		print(formulario.cleaned_data)

		datos_formulario = formulario.cleaned_data
		nombre_obtenido = datos_formulario.get("nombre_form")
		contrasena_obtenida = datos_formulario.get("contrasena_form")

		objeto_usuario = Usuario.objects.get(nombre = nombre_obtenido)

		if contrasena_obtenida == objeto_usuario.contrasena:
			return HttpResponseRedirect(reverse('inicio'))

	return render(request, "iniciar_sesion.html", contexto)

def InicioView(request):
	return render(request, "inicio.html", {})
<<<<<<< HEAD
=======

def RegistrarProveedorView(request):
	formulario = RegistrarProveedorForm(request.POST or None)
	contexto = { "formulario" : formulario }

	if formulario.is_valid():
		print(formulario.cleaned_data)

		datos_formulario = formulario.cleaned_data
		nombre_obtenido = datos_formulario.get("nombre_form")
		telefono_obtenido = datos_formulario.get("telefono_form")
		direccion_obtenida = datos_formulario.get("direccion_form")
		email_obtenido = datos_formulario.get("email_form")

		objeto_proveedor = Proveedor.objects.create(nombre = nombre_obtenido, telefono = telefono_obtenido, direccion = direccion_obtenida, email = email_obtenido)

		return HttpResponseRedirect(reverse('inicio'))
		
	return render(request, "registrar_proveedor.html", contexto)
>>>>>>> jonathan
