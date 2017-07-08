from django import forms
from .models import *

OPCIONES_ANOS = ('2012','2013','2014','2015','2016', '2017', '2018', '2019', '2020', '2021')
OPCIONES_MESES = ('January', 'February', 'March', 'April', 'May')


class registrarProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    telefono = forms.IntegerField()
    direccion = forms.CharField()
    correo = forms.EmailField()


class registrarProveedorProductoForm(forms.Form):

    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    fecha_tiempo = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))


class registrarUsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    contrasena = forms.CharField(max_length=20, widget=forms.PasswordInput())
    correo = forms.EmailField()

# OPCIONES_ANOS = ('2016', '2017') #añadido para probar pedidos


class registrarPedidoForm(forms.Form):
    producto = forms.CharField(max_length=20)
    proveedor = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    fecha_prevista = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))  # añadido para probar pedidos
    fecha_recibida = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))  # añadido para probar pedidos
    fecha_realizada = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))  # añadido para probar pedidos


class registrarOrdenForm(forms.Form):
    producto = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    fecha = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))
    precio_unidad = forms.IntegerField()
    precio_total = forms.IntegerField()


class seleccionarTipoPedidoForm(forms.Form):
    todos = 'todos_los_pedidos'
    no_recibido = 'pedidos_no_recibidos'
    recibido = 'pedidos_recibidos'

    pedido_choice = ((todos, u"Todos los pedidos"),
                     (no_recibido, u"Pedidos no recibidos"),
                     (recibido, u"Pedidos recibidos"))

    tipo_pedido = forms.ChoiceField(choices=pedido_choice)


class eliminarPedidosForm(forms.Form):
    eliminar = 'eliminar'
    corregir = 'corregir'

    solucion_pedidos_choice = ((eliminar, u"Eliminar"),
                               (corregir, u"Corregir"))

    solucion_pedidos = forms.ChoiceField(choices=solucion_pedidos_choice)


class recibirPedidoForm(forms.Form):
    id_pedido = forms.IntegerField()
    fecha_recibida = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))


class reporteProductoForm(forms.Form):
    inicio = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))
    fin = forms.DateField(widget=forms.SelectDateWidget(years=OPCIONES_ANOS))


class reporteProveedorForm(forms.Form):
    inicio = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))
    fin = forms.DateField(widget=forms.SelectDateWidget(years=OPCIONES_ANOS))


class registrarProductoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    codigo = forms.CharField(max_length=20)
    valor = forms.IntegerField()
    fecha_ingreso = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))


class graficarProductoForm(forms.Form):
    inicio = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))
    nombre = forms.CharField(max_length=20)
    codigo = forms.CharField(max_length=20)
    valor = forms.IntegerField()
    fecha_ingreso = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))


class seleccionarTipoReporteMovimiento(forms.Form):
    diario = 'diario'
    mensual = 'mensual'
    anual = 'anual'

    reporte_choice = ((diario, u"Reporte diario"),
                      (mensual, u"Reporte mensual"),
                      (anual, u"Reporte anual"))
    producto = forms.CharField(max_length=20)
    tipo_reporte = forms.ChoiceField(choices=reporte_choice)
    fecha_inicial = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))
    fecha_final = forms.DateField(
        widget=forms.SelectDateWidget(
            years=OPCIONES_ANOS))


class tiempo_pedido_form(forms.Form):
    a_tiempo = "atiempo"
    con_retraso = "conretraso"
    reporte_choice = ((a_tiempo, u"Llego a tiempo"),
                      (con_retraso, u"Llego con retraso"))
    opcion_tiempo = forms.ChoiceField(choices=reporte_choice)


class mostrarPedidoForm(forms.Form):
    producto = forms.CharField(max_length=20)


class seleccionarAnalisisOrdenForm(forms.Form):
    ordenes = 'ordenes'
    analisis = 'analisis'

    orden_analisis_choice = ((ordenes, u"Todas las Ordenes"),
                             (analisis, u"Analisis ABC"))

    ver = forms.ChoiceField(choices=orden_analisis_choice)
