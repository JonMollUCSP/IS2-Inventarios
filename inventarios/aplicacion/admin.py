from django.contrib import admin

from .models import Usuario

class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "contrasena", "email"]

	class Meta:
		model = Usuario

admin.site.register(Usuario, AdminUsuario)
