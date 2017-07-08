from django.contrib import admin

from .models import *


class AdminProveedor(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "telefono", "direccion", "correo"]

    class Meta:
        model = Proveedor


admin.site.register(Proveedor, AdminProveedor)


class AdminAlmacen(admin.ModelAdmin):
    list_display = ["__str__", "anaqueles_por_fila", "direccion", "filas"]

    class Meta:
        model = Almacen


admin.site.register(Almacen, AdminAlmacen)


class AdminPedido(admin.ModelAdmin):
    list_display = [
        "__str__",
        "proveedor",
        "fecha_realizada",
        "fecha_prevista",
        "fecha_recibida",
        "cantidad"]

    class Meta:
        model = Pedido


admin.site.register(Pedido, AdminPedido)


class AdminProducto(admin.ModelAdmin):

    list_display = ["__str__", "nombre", "codigo", "valor"]

    class Meta:
        model = Producto


admin.site.register(Producto, AdminProducto)


class AdminProveedorProducto(admin.ModelAdmin):

    list_display = ["__str__", "proveedor", "producto", "fecha_tiempo"]

    class Meta:
        model = ProveedorProducto


admin.site.register(ProveedorProducto, AdminProveedorProducto)
