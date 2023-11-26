from django import forms
from django.core.exceptions import ValidationError
from .models import Ingresos, Empleado, Cliente, Material, Posiciones, Stock


# Ingreso de materiales


class IngresosForm(forms.Form):
    remito_fc = forms.CharField(label="Remito / FC")
    fecha_ingreso = forms.DateField(
        label="Fecha de ingreso", widget=forms.SelectDateWidget())


# Alta de usuarios


class TipoUsuarioForm(forms.Form):
    tipos = [
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
    ]
    tipo = forms.ChoiceField(
        choices=tipos, widget=forms.RadioSelect, required=False)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class StockForm(forms.Form):
    material = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all())
    cantidad = forms.IntegerField(label="Cantidad")
    posicion = forms.ModelMultipleChoiceField(
        queryset=Posiciones.objects.all())


class Material(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        error_messages = {
            'sku': {'required': 'Debe completar SKU'}
        }


class PosicionForm(forms.Form):
    posicion = forms.CharField(label="Ubicación", max_length=10)
    estado = forms.CharField(
        label="Estado de la posición", max_length=8)
