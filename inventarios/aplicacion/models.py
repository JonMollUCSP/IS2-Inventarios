from django.db import models

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

class Producto(models.Model):
	id = models.AutoField(primary_key= True)
	nombre = models.CharField(max_length = 20)
	tipo = models.CharField(max_length = 20)
	valor = models.IntegerField()
	
	def __str__(self):
		return self.nombre

class ProveedorProducto(models.Model):
	id = models.AutoField(primary_key=True)
	proveedor = models.ForeignKey(Proveedor)
	producto = models.ForeignKey(Producto)
	fecha_tiempo = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre

class Almacen(models.Model):
	anaqueles_por_fila = models.IntegerField()
	direccion = models.TextField()
	filas = models.IntegerField()

	def __str__(self):
		return self.direccion

class Pedido(models.Model):
	proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
	#producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	fechaRealizada = models.DateField(null = True)
	fechaPrevista = models.DateField(null = True)
	fechaRecibida = models.DateField(null = True)
	cantidad = models.CharField(max_length = 10)

	def _str_(self):
		return self.cantidad
