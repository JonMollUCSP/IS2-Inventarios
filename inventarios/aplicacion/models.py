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

class Pedido(models.Model):
	proveedor 		= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	#producto		= models.ForeignKey(Producto, on_delete=models.CASCADE)
	fechaRealizada 	= models.DateField(null=True)
	fechaPrevista 	= models.DateField(null=True)
	fechaRecibida	= models.DateField(null=True)
	cantidad		= models.CharField(max_length=10)

	def __str__(self):
		return self.cantidad
