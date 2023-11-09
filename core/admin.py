from django.contrib import admin
from core.models import Empleado, Cliente, EmpleadoCliente, Posiciones, Stock, Material, Ingresos

# Register your models here.


class IngresoAdmin(admin.ModelAdmin):
    list_display = ('remito_fc', 'fecha_ingreso')
    list_editable = ['remito_fc']
    list_display_links = ['fecha_ingreso']
    search_fields = ['remito_fc']


admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(EmpleadoCliente)
admin.site.register(Posiciones)
admin.site.register(Stock)
admin.site.register(Material)
admin.site.register(Ingresos, IngresoAdmin)
