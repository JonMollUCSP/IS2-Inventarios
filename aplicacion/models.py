from django.db import models
from datetime import date


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class SubGrupo(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)

    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    s_grupo = models.ForeignKey(SubGrupo, on_delete=models.SET_NULL, null=True)
    fecha_ingreso = models.DateField(null=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    ultima_clasificacion = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(
        Producto,
        through='ProveedorProducto',
        related_name='prods+')
    pedidos = models.ManyToManyField(
        Producto, through='Pedido', related_name='peds+')

    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.TextField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class Almacen(models.Model):
    id = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(Producto, through='AnaquelProducto')

    anaqueles_por_fila = models.IntegerField()
    direccion = models.TextField()
    filas = models.IntegerField()

    def __str__(self):
        return self.direccion


class ProveedorProducto(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)

    fecha_tiempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.proveedor.nombre


class AnaquelProducto(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)
    grupo = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True)

    numero = models.IntegerField()
    fila = models.IntegerField()
    cantidad_max = models.IntegerField()
    candidad_producto = models.IntegerField()

    def __str__(self):
        return self.producto.nombre


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True)

    fecha_realizada = models.DateField(default=date.today, null=True)
    fecha_prevista = models.DateField(null=True)
    fecha_recibida = models.DateField(null=True)
    cantidad = models.CharField(max_length=10)

    def __str__(self):
        return self.producto.nombre


class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)

    fecha = models.DateField(default=date.today)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre
