from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *

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
