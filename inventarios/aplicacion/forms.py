from django import forms

class IniciarSesionForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	contrasena_form = forms.CharField(max_length = 20)

class RegistrarProductoForm(forms.Form):
        nombre_form = forms.CharField(max_length = 20)
        tipo_form =  forms.CharField(max_length = 20)
        valor_form = forms.IntegerField()

class RegistrarProveedorForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	telefono_form = forms.IntegerField()
	direccion_form = forms.CharField()
	email_form = forms.EmailField()

class RegistrarUsuarioForm(forms.Form):
	nombre_form=forms.CharField(max_length=20)
	contrasena_form=forms.CharField(max_length=20)
	email_form=forms.EmailField()

class RegistrarPedidoForm(forms.Form):
	producto_form = forms.CharField(max_length=20)
	proveedor_form = forms.CharField(max_length=20)
	cantidad_form = forms.IntegerField()
	fecha_prevista_form = forms.DateField()

class SeleccionarTipoPedidoForm(forms.Form):
	todos = 'todos_los_pedidos'
	no_recibido = 'pedidos_no_recibidos'
	recibido = 'pedidos_recibidos'
	pedido_choice = (
		(todos, u"Todos los pedidos"),
		(no_recibido, u"Pedidos no recibidos"),
		(recibido, u"Pedidos recibidos")
	)
	tipo_pedido_form = forms.ChoiceField(choices=pedido_choice)

class RecibirPedidoForm(forms.Form):
	id_pedido_form = forms.IntegerField()
	fecha_recibida_form = forms.DateField()
