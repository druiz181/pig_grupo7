from django import forms

class IngresosForm(forms.Form):
    remito_fc = forms.CharField(label="Remito / FC")
    fecha_igreso = forms.DateField(label="Fecha de ingreso", widget=forms.SelectDateWidget())
    sku = forms.CharField(label="SKU", required=True)
    descripcion = forms.CharField(label="Descripción")
    cantidad = forms.IntegerField(label="Cantidad", required=True)

