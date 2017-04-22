from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import *
from .models import *

def InicioView(request):
	return render(request, "inicio.html", {})

from .forms import IniciarSesionForm
from .models import Usuario
from .models import Pedido


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


def ProveedorView(request):
	proveedores = Proveedor.objects.all()
	contexto = { "proveedores" : proveedores }
	
	return render(request, "proveedor.html", contexto)

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

def InicioView(request):
	return render(request, "inicio.html", {})

def PedidosView(request):
	query = Pedido.objects.all()
	# data = []
	# for row in rows:
	# 	data.append(row)

	return render(request, 'pedidos.html',{'pedidos':query})



