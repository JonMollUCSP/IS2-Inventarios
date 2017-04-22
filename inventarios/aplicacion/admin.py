from django.contrib import admin

from .models import Usuario
from .models import Proveedor

class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "contrasena", "email"]

	class Meta:
		model = Usuario

admin.site.register(Usuario, AdminUsuario)

class AdminProveedor(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "telefono","direccion","email"]

	class Meta:
		model = Proveedor

admin.site.register(Proveedor,AdminProveedor)
