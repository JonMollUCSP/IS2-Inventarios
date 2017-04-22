from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .forms import IniciarSesionForm
from .models import Usuario
from .models import Almacen

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



def AlmacenView(request):
    almacen=Almacen.objects.all() 
    return render(request,"lista_tipo_almacen.html",{"almacen":almacen})

    

