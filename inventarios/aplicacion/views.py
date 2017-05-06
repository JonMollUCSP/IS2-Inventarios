from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *

def InicioView(request):
	return render(request, "inicio.html", {})

def IniciarSesionView(request):
        formulario = IniciarSesionForm(request.POST or None)
        contexto = { "formulario" : formulario }

        if formulario.is_valid():
                print(formulario.cleaned_data)
                datos_formulario = formulario.cleaned_data
                nombre_obtenido = datos_formulario.get("nombre_form")
                contrasena_obtenida = datos_formulario.get("contrasena_form")

                objeto_usuario = Usuario.objects.get(nombre = nombre_obtenido)
                datos_formulario = formulario.cleaned_data
                nombre_obtenido = datos_formulario.get("nombre_form")
                contrasena_obtenida = datos_formulario.get("contrasena_form")
                objeto_usuario = Usuario.objects.get(nombre = nombre_obtenido)

                if contrasena_obtenida == objeto_usuario.contrasena:
                        return HttpResponseRedirect(reverse('inicio'))

        return render(request, "iniciar_sesion.html", contexto)


def mostrarProductoView(request):
        productos = Producto.objects.all()
        contexto = { "productos" : productos }
        return render(request,"mostrarProducto.html",contexto)

def registrarProductoView(request):
        formulario = RegistrarProductoForm(request.POST or None)
        contexto = { "formulario" : formulario }
        if formulario.is_valid():
                print(formulario.cleaned_data)
                datos_formulario = formulario.cleaned_data
                nombre_obtenido = datos_formulario.get("nombre_form")
                tipo_obtenido = datos_formulario.get("tipo_form")
                valor_obtenido = datos_formulario.get("valor_form")
                objeto_proveedor = Producto.objects.create(nombre = nombre_obtenido, tipo = tipo_obtenido, valor = valor_obtenido)
                return HttpResponseRedirect(reverse('inicio'))	
        return render(request, "registrarProducto.html", contexto)
def ProveedorView(request):
	proveedores = Proveedor.objects.all()
	contexto = { "proveedores" : proveedores }
	
	return render(request, "proveedor.html", contexto)

def RegistrarProveedorView(request):
	formulario = RegistrarProveedorForm(request.POST or None)
	contexto = { "formulario" : formulario }

	if formulario.is_valid():
		print(formulario.cleaned_data)

		datos_formulario = formulario.cleaned_data
		nombre_obtenido = datos_formulario.get("nombre_form")
		telefono_obtenido = datos_formulario.get("telefono_form")
		direccion_obtenida = datos_formulario.get("direccion_form")
		email_obtenido = datos_formulario.get("email_form")

		objeto_proveedor = Proveedor.objects.create(nombre = nombre_obtenido, telefono = telefono_obtenido, direccion = direccion_obtenida, email = email_obtenido)

		return HttpResponseRedirect(reverse('inicio'))
		
	return render(request, "registrar_proveedor.html", contexto)

def AlmacenView(request):
    almacenes = Almacen.objects.all()
    contexto = { "almacenes" : almacenes }

    return render(request, "almacen.html", contexto)

def PedidoView(request):
	formulario_tipo_de_pedido = SeleccionarTipoPedidoForm(request.POST or None)

	if formulario_tipo_de_pedido.is_valid():
		print(formulario_tipo_de_pedido.cleaned_data)
		datos_formulario = formulario_tipo_de_pedido.cleaned_data
		tipo_pedido_obtenido = datos_formulario.get("tipo_pedido_form")
		if tipo_pedido_obtenido == 'pedidos_recibidos':
			pedidos = Pedido.objects.filter(fecha_recibida__isnull=False)
		if tipo_pedido_obtenido == 'pedidos_no_recibidos':
			pedidos = Pedido.objects.filter(fecha_recibida__isnull=True)
	else:
		pedidos = Pedido.objects.all()

	contexto = {"formulario_tipo_de_pedido" : formulario_tipo_de_pedido, "pedidos" : pedidos}
	return render(request, "pedido.html", contexto)

def registrarPedidoView(request):
	formulario = RegistrarPedidoForm(request.POST or None)
	contexto = { "formulario" : formulario }

	if formulario.is_valid():
		print(formulario.cleaned_data)

		datos_formulario = formulario.cleaned_data
		producto_obtenido = datos_formulario.get("producto_form")
		proveedor_obtenido = datos_formulario.get("proveedor_form")
		cantidad_obtenida = datos_formulario.get("cantidad_form")
		fecha_prevista_obtenida = datos_formulario.get("fecha_prevista_form")
		producto = Producto.objects.get(nombre=producto_obtenido)
		proveedor = Proveedor.objects.get(nombre=proveedor_obtenido)

		objecto_pedido = Pedido.objects.create(proveedor=proveedor, producto=producto, fechaPrevista=fecha_prevista_obtenida, cantidad=cantidad_obtenida)

		return HttpResponseRedirect(reverse('inicio'))

	return render(request, "registrar_pedido.html", contexto)

def RegistrarUsuarioView(request):
    formulario = RegistrarUsuarioForm(request.POST or None)
    contexto = { "formulario" : formulario }

    if formulario.is_valid():
        print(formulario.cleaned_data)

        datos_formulario = formulario.cleaned_data
        nombre_obtenido = datos_formulario.get("nombre_form")
        contrasena_obtenido=datos_formulario.get("contrasena_form")
        email_obtenido = datos_formulario.get("email_form")

        objeto_usuario = Usuario.objects.create(nombre = nombre_obtenido, contrasena=contrasena_obtenido, email = email_obtenido)

        return HttpResponseRedirect(reverse('inicio'))
        
    return render(request, "usuario_form.html", contexto)

def ReporteProductoView(request):
    from django.db import connection
    cursor = connection.cursor()

    formulario = ReporteProductoForm(request.POST)
  
    if formulario.is_valid():
        print(formulario.cleaned_data)
        datos_formulario = formulario.cleaned_data
        mes = datos_formulario.get('DateField', 'month')
        
    cursor.execute("SELECT aplicacion_producto.nombre, cantidad, fecha_recibida, aplicacion_proveedor.nombre FROM aplicacion_pedido INNER JOIN aplicacion_producto ON aplicacion_pedido.producto_id = aplicacion_producto.id INNER JOIN aplicacion_proveedor ON aplicacion_pedido.proveedor_id = aplicacion_proveedor.id;")
    productos = cursor.fetchall()
    contexto = { "formulario" : formulario,"productos":productos }
    return render(request, "reporteProductos.html", contexto)

def ProveedorProductoView(request,id_propro):
	productos = Producto.objects.filter(proveedorproducto__producto__id__isnull=False,
        proveedorproducto__proveedor__id=id_propro)
	contexto = { "productos" : productos }
        
	return render(request, "proveedorproducto.html", contexto)



