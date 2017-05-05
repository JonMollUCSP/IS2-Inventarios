from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import arrow
from .forms import *
from datetime import *
from .models import *

def InicioView(request):
	return render(request, "inicio.html", {})

def IniciarSesionView(request):
        formulario = IniciarSesionForm(request.POST or None)
        contexto = { "formulario" : formulario }

        if formulario.is_valid():
                print(formulario.cleaned_data)
                datos_formulario = formulario.cleaned_data
                nombre_obtenido = datos_formulario.get("nombre_form")
                contrasena_obtenida = datos_formulario.get("contrasena_form")

                objeto_usuario = Usuario.objects.get(nombre = nombre_obtenido)
                datos_formulario = formulario.cleaned_data
                nombre_obtenido = datos_formulario.get("nombre_form")
                contrasena_obtenida = datos_formulario.get("contrasena_form")
                objeto_usuario = Usuario.objects.get(nombre = nombre_obtenido)

                if contrasena_obtenida == objeto_usuario.contrasena:
                        return HttpResponseRedirect(reverse('inicio'))

        return render(request, "iniciar_sesion.html", contexto)


def mostrarProductoView(request):
        productos = Producto.objects.all()
        contexto = { "productos" : productos }
        return render(request,"mostrarProducto.html",contexto)

def registrarProductoView(request):
        formulario = RegistrarProductoForm(request.POST or None)
        contexto = { "formulario" : formulario }
        if formulario.is_valid():
                print(formulario.cleaned_data)
                datos_formulario = formulario.cleaned_data
                nombre_obtenido = datos_formulario.get("nombre_form")
                tipo_obtenido = datos_formulario.get("tipo_form")
                valor_obtenido = datos_formulario.get("valor_form")
                objeto_proveedor = Producto.objects.create(nombre = nombre_obtenido, tipo = tipo_obtenido, valor = valor_obtenido)
                return HttpResponseRedirect(reverse('inicio'))	
        return render(request, "registrarProducto.html", contexto)
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

def AlmacenView(request):
    almacenes = Almacen.objects.all()
    contexto = { "almacenes" : almacenes }

    return render(request, "almacen.html", contexto)

def PedidoView(request):
	pedidos = Pedido.objects.all()
	contexto = { 'pedidos' : pedidos }

	return render(request, 'pedido.html', contexto)

def RegistrarUsuarioView(request):
    formulario = RegistrarUsuarioForm(request.POST or None)
    contexto = { "formulario" : formulario }

    if formulario.is_valid():
        print(formulario.cleaned_data)

        datos_formulario = formulario.cleaned_data
        nombre_obtenido = datos_formulario.get("nombre_form")
        contrasena_obtenido=datos_formulario.get("contrasena_form")
        email_obtenido = datos_formulario.get("email_form")

        objeto_usuario = Usuario.objects.create(nombre = nombre_obtenido, contrasena=contrasena_obtenido, email = email_obtenido)

        return HttpResponseRedirect(reverse('inicio'))
        
    return render(request, "usuario_form.html", contexto)


def mostrarfechaPedido(request):
    formulario= PedidoForm(request.POST or None)
    contexto={"formulario":formulario}
    if formulario.is_valid():
        print(formulario.cleaned_data)
        datos_formulario=formulario.cleaned_data
        f_inicial=datos_formualrio.get("fechaRealizada")
        f_cierre=datos_formualrio.get("fechaRealizada")
        rango_fecha=Pedido.objects.filter(fecha__range=(f_inicial,f_cierre))
        return HttpResponseRedirect(reverse('inicio'))
    return render(request,"graficos2.html",contexto)

