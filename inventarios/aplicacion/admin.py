from django.contrib import admin

from .models import Usuario
from .models import Pedido

class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "contrasena", "email"]

	class Meta:
		model = Usuario

class AdminPedido(admin.ModelAdmin):
	list_display = ["proveedor",
					"fechaRealizada",
					"fechaPrevista",
					"fechaRecibida",
					"cantidad"
					]
	class Meta:
		model = Pedido

admin.site.register(Pedido, AdminPedido)
admin.site.register(Usuario, AdminUsuario)
