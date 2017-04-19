from django.shortcuts import render
from .forms import LoginForm
from .models import Usuario

def login(request):
	form = LoginForm()
	context = {
		"form" : form
	}

	if form.is_valid():
		form_data = form.cleaned_data
		nombre_form = form_data.get("nombre_form")
		contrasena_form = form_data.get("contrasena_form")

		objeto = Usuario.objects.get(nombre = nombre_form)

		if contrasena_form == objeto.contrasena:
			return render(request, "inicio.html", {})

	return render(request, "login.html", context)

def inicio(request):
	return render(request, "inicio.html", {})
