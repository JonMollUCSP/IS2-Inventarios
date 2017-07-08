# interfaz repositorio (@Query's (filter, all) de entidades 'models')
from django.db import models
from .models import Pedido, Producto


class PedidoRepositorio():

    def getPedidosRecibidosDiarios(self, producto, fecha_inicial, fecha_final):
        return Pedido.objects.values('fecha_recibida').filter(
            producto=producto.id, fecha_recibida__isnull=False, fecha_recibida__range=(
                fecha_inicial, fecha_final)).annotate(
            pedidos_count=models.Count('fecha_recibida')).annotate(
            cantidad_parcial=models.Sum(models.functions.Cast(
                'cantidad', models.IntegerField()))).order_by('-fecha_recibida')

    def updateFechaRecibidaId(self, id_pedido, fecha_recibida):
        Pedido.objects.filter(
            id=id_pedido).update(
            fecha_recibida=fecha_recibida)

    def updateCantidad(self, id_pedido, cantidad):
        Pedido.objects.filter(
            id=id_pedido).update(
            cantidad=cantidad)

    def getPedidosNoRecibidos(self):
        return Pedido.objects.filter(fecha_recibida__isnull=True)

    def getPedidosRecibidosProducto(self, producto):
        return Pedido.objects.filter(
            producto=producto.id,
            fecha_recibida__isnull=False)

    def getPedidosRecibidos(self):
        return Pedido.objects.filter(fecha_recibida__isnull=False)

    def getPedidos(self):
        return Pedido.objects.all()


class ProductoRepositorio():

    def getProductos(self):
        return Producto.objects.all()
