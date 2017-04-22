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

class Almacen(models.Model):
	anaqueles_por_fila =models.IntegerField()
	direccion=models.TextField()
	filas=models.IntegerField()

	def __str__(self):
		return self.direccion
		

		