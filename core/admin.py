from django.contrib import admin
from core.models import Empleado, Cliente, EmpleadoCliente, Posiciones, Stock, Material, Ingresos

# Register your models here.


class IngresoAdmin(admin.ModelAdmin):
    list_display = ('remito_fc', 'fecha_ingreso')
    list_editable = ['remito_fc']
    list_display_links = ['fecha_ingreso']
    search_fields = ['remito_fc']


class StockAdmin(admin.ModelAdmin):
    list_display = ('posicion', 'material', 'cantidad')
    list_editable = ['posicion', 'cantidad']
    list_display_links = ['material']
    search_fields = ['material.sku']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('sku', 'descripcion')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'material':
            kwargs["queryset"] = Material.objects.filter().order_by("sku")

        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(EmpleadoCliente)
admin.site.register(Posiciones)
admin.site.register(Stock, StockAdmin)
# admin.site.register(Material, MaterialAdmin)
admin.site.register(Ingresos, IngresoAdmin)
