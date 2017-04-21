from django.shortcuts import render
from .forms import LoginForm
from .models import Usuario

from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
	form = LoginForm(request.POST or None)
	context = {
		"form" : form
	}

	if form.is_valid():
		print(form.cleaned_data)

		form_data = form.cleaned_data
		nombre_get = form_data.get("nombre_form")
		contrasena_get = form_data.get("contrasena_form")

		objeto = Usuario.objects.get(nombre = nombre_get)

		if contrasena_get == objeto.contrasena:
			return HttpResponseRedirect(reverse('inicio'))

	return render(request, "login.html", context)

def inicio(request):
	return render(request, "inicio.html", {})
