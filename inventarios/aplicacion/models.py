from django.db import models
from datetime import date

class Usuario(models.Model):
	nombre = models.CharField(max_length = 20)
	contrasena = models.CharField(max_length = 20)
	email = models.EmailField()

	def __str__(self):
		return self.nombre


class Proveedor(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length = 20)
	telefono = models.IntegerField()
	direccion = models.TextField()
	email = models.EmailField()

	def __str__(self):
		return self.nombre
class Almacen(models.Model):
	anaqueles_por_fila = models.IntegerField()
	direccion = models.TextField()
	filas = models.IntegerField()

	def __str__(self):
		return self.direccion

class Producto(models.Model):
        id = models.AutoField(primary_key= True)
        nombre = models.CharField(max_length = 20)
        tipo = models.CharField(max_length = 20)
        valor = models.IntegerField()
        fecha = models.DateTimeField(auto_now_add=True)
        cantidad = models.IntegerField()
        # localizacion = models.CharField(max_length=100)
        #falta fk para clasificacion
        #falta fk para grupo
        almacenAsoc = models.ForeignKey(Almacen, on_delete=models.CASCADE, null=True)
        
        def __str__(self):
                return self.nombre        

class ProveedorProducto(models.Model):
	id = models.AutoField(primary_key=True)
	proveedor = models.ForeignKey(Proveedor)
	producto = models.ForeignKey(Producto)
	fecha_tiempo = models.DateTimeField(auto_now_add=True)

	"""def __str__(self):
		return self.id"""


class Pedido(models.Model):
	id = models.AutoField(primary_key=True)
	proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
	fecha_realizada = models.DateField(default=date.today, null = True)
	fecha_prevista = models.DateField(null = True)
	fecha_recibida = models.DateField(null = True)
	cantidad = models.CharField(max_length = 10)

	def _str_(self):
		return self.cantidad
