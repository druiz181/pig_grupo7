from django import forms
from django.core.exceptions import ValidationError
from .models import Materiales, Empleado, Cliente

#Ingreso de materiales
class IngresosForm(forms.Form):
    remito_fc = forms.CharField(label="Remito / FC")
    fecha_ingreso = forms.DateField(label="Fecha de ingreso", widget=forms.SelectDateWidget())
    sku = forms.CharField(label="SKU", required=True)
    descripcion = forms.CharField(label="Descripción")
    cantidad = forms.IntegerField(label="Cantidad", required=True)

    def clean_cantidad(self):
        if self.cleaned_data["cantidad"] < 1:
            raise ValidationError("Ingrese cantidad")
        
        return self.cleaned_data["cantidad"] 
    
# Alta de usuarios
class TipoUsuarioForm(forms.Form):
    tipos = [
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
    ]
    tipo = forms.ChoiceField(choices=tipos, widget=forms.RadioSelect, required=False)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


