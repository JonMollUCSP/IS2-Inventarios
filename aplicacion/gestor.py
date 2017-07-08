# interfaz gestor (Gestion para interfaces 'views')
from .repositorio import PedidoRepositorio, ProductoRepositorio
from decimal import Decimal

# gestion de vista reporteMovimientoView


class GestorReporte:

    def getFecha(self, movimiento, tipo_reporte):
        year = movimiento.get('fecha_recibida').year
        if tipo_reporte == 'anual':
            return str(year)
        month = movimiento.get('fecha_recibida').strftime("%B")
        return str(month) + ", " + str(year)

    def getMovimiento(self, fecha_recibida, cantidad):
        movimiento = {
            "fecha_recibida": fecha_recibida,
            "cantidad_parcial": cantidad}
        return movimiento

    def getMovimientosMensualOAnual(self, movimientos, tipo_reporte):
        movimientos_acumulados = []
        fecha_recibida = None
        cantidad = 0
        for movimiento in movimientos:
            fecha_movimiento = self.getFecha(movimiento, tipo_reporte)
            if(fecha_recibida is not None and fecha_movimiento != fecha_recibida):
                movimientos_acumulados.append(
                    self.getMovimiento(fecha_recibida, cantidad))
                cantidad = 0
            fecha_recibida = fecha_movimiento
            cantidad += movimiento.get('cantidad_parcial')
        if(fecha_recibida is not None):
            movimientos_acumulados.append(
                self.getMovimiento(
                    fecha_recibida, cantidad))
        return movimientos_acumulados

    def getMovimientos(
            self,
            producto,
            fecha_inicial,
            fecha_final,
            tipo_reporte):
        pedidoRepositorio = PedidoRepositorio()
        movimientos = pedidoRepositorio.getPedidosRecibidosDiarios(
            producto, fecha_inicial, fecha_final)
        if(tipo_reporte != "diario"):
            movimientos = self.getMovimientosMensualOAnual(
                movimientos, tipo_reporte)
        for movimiento in movimientos:
            movimiento['monto_total'] = "$" + \
                str(Decimal(movimiento.get('cantidad_parcial'))
                    * Decimal(producto.valor))
        return movimientos

    def getProductosConMovimiento(self):
        productoRepositorio = ProductoRepositorio()
        pedidoRepositorio = PedidoRepositorio()
        productos = productoRepositorio.getProductos()
        for producto in productos:
            monto_total = Decimal(0)
            pedidos = pedidoRepositorio.getPedidosRecibidosProducto(producto)
            monto_total_correcto=-1
            for pedido in pedidos:
                if (pedido.cantidad.isdigit()):
                    monto_total = monto_total + \
                        Decimal(pedido.cantidad) * Decimal(producto.valor)
                else:
                    monto_total_correcto= pedido.id
            if monto_total_correcto==-1:
                producto.monto_total = "$" + str(monto_total)
            else:
                producto.monto_total = "$" +str(monto_total) + " (Error pedido " + str(monto_total_correcto) + ")"
        return productos


class TodosLosPedidos():

    def obtenerPedidos(self):
        return PedidoRepositorio().getPedidos()


class PedidosRecibidos():

    def obtenerPedidos(self):
        return PedidoRepositorio().getPedidosRecibidos()


class PedidosNoRecibidos():

    def obtenerPedidos(self):
        return PedidoRepositorio().getPedidosNoRecibidos()


class GestorDePedidos():

    def __init__(self):
        self.tipos_de_pedido = {
            'todos_los_pedidos': TodosLosPedidos(),
            'pedidos_recibidos': PedidosRecibidos(),
            'pedidos_no_recibidos': PedidosNoRecibidos()}

    def obtenerPedidosTipo(self, tipo_pedido):
        return self.tipos_de_pedido.get(tipo_pedido).obtenerPedidos()

    def updateFechaRecibidaId(self, id_pedido, fecha_recibida):
        PedidoRepositorio.updateFechaRecibidaId(
            self, id_pedido, fecha_recibida)

    def updateCantidadFirstCharacter(self):
        print ("corrigiendo cantidad")
        pedidoRepositorio=PedidoRepositorio()
        pedidos = pedidoRepositorio.getPedidos()
        for pedido in pedidos:
            cantidad = ord(pedido.cantidad[0])
            pedidoRepositorio.updateCantidad(
                pedido.id, cantidad)
