from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length = 20)
	contrasena = models.CharField(max_length = 20)
	email = models.EmailField()

	def __str__(self):
		return self.nombre

class Proveedor(models.Model):
	nombre = models.CharField(max_length = 20)
	telefono = models.IntegerField()
	direccion = models.TextField()
	email = models.EmailField()

	def __str__(self):
		return self.nombre

class Producto(models.Model):
        nombre = models.CharField(max_length = 20)
        tipo = models.CharField(max_length = 20)
        valor = models.IntegerField()
class Almacen(models.Model):
	anaqueles_por_fila = models.IntegerField()
	direccion = models.TextField()
	filas = models.IntegerField()

	def __str__(self):
		return self.direccion

class Pedido(models.Model):
	proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
	fechaRealizada = models.DateField(null = True)
	fechaPrevista = models.DateField(null = True)
	fechaRecibida = models.DateField(null = True)
	cantidad = models.CharField(max_length = 10)

	def _str_(self):
		return self.cantidad

class ReporteProducto(models.Model):
	ID = models.CharField(max_length = 20)
	nombre = models.CharField(max_length = 20)
	fechaRealizada = models.CharField(max_length = 20)
	cantidad = models.CharField(max_length = 20)
	almacen = models.CharField(max_length = 20)
	tipo = models.CharField(max_length = 20)
	class Meta:
		managed = False
