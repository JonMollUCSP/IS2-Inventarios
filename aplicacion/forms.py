from django import forms

class iniciarSesionForm(forms.Form):
	nombre = forms.CharField(max_length = 20)
	contrasena = forms.CharField(max_length = 20)

class registrarProveedorForm(forms.Form):
	nombre = forms.CharField(max_length = 20)
	telefono = forms.IntegerField()
	direccion = forms.CharField()
	correo = forms.EmailField()

class registrarUsuarioForm(forms.Form):
	nombre = forms.CharField(max_length = 20)
	contrasena = forms.CharField(max_length = 20)
	correo = forms.EmailField()

class registrarPedidoForm(forms.Form):
	producto = forms.CharField(max_length = 20)
	proveedor = forms.CharField(max_length = 20)
	cantidad = forms.IntegerField()

class seleccionarTipoPedidoForm(forms.Form):
	todos = 'todos_los_pedidos'
	no_recibido = 'pedidos_no_recibidos'
	recibido = 'pedidos_recibidos'

	pedido_choice = ((todos, u"Todos los pedidos"),
                     (no_recibido, u"Pedidos no recibidos"),
                     (recibido, u"Pedidos recibidos"))

	tipo_pedido = forms.ChoiceField(choices = pedido_choice)

class recibirPedidoForm(forms.Form):
	id_pedido = forms.IntegerField()
	fecha_recibida = forms.DateField()

OPCIONES_ANOS = ('2016', '2017')
OPCIONES_MESES = ('January', 'February', 'March', 'April', 'May')
class reporteProductoForm(forms.Form):
        inicio = forms.DateField(widget = forms.SelectDateWidget(years = OPCIONES_ANOS))
        fin = forms.DateField(widget = forms.SelectDateWidget(years = OPCIONES_ANOS))

class registrarProductoForm(forms.Form):
        nombre = forms.CharField(max_length = 20)
        codigo = forms.CharField(max_length = 20)
        valor = forms.IntegerField()
        fecha_ingreso = forms.DateField(widget = forms.SelectDateWidget(years = OPCIONES_ANOS))

class seleccionarTipoReporteMovimiento(forms.Form):
	diario = 'diario'
	mensual = 'mensual'
	anual = 'anual'

	reporte_choice = ((diario, u"Reporte diario"),
                     (mensual, u"Reporte mensual"),
                     (anual, u"Reporte anual"))
	tipo_reporte = forms.ChoiceField(choices = reporte_choice)
	fecha_inicial = forms.DateField(widget = forms.SelectDateWidget(years = OPCIONES_ANOS))
	fecha_final = forms.DateField(widget = forms.SelectDateWidget(years = OPCIONES_ANOS))

