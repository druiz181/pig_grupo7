from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    email = models.EmailField(blank=False, verbose_name="Email")

    def clean_dni(self):
        if not (9999999 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("Ingrese un DNI válido")
        return self.cleaned_data['dni']

    class Meta:
        abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.nombre_completo


class Cliente(Usuario):
    tipo_cliente = models.CharField(max_length=20, choices=[
        ('individual', 'Individual'),
        ('empresa', 'Empresa')])

    empresa = models.CharField(
        max_length=50, verbose_name="Empresa", null=True)


class Empleado(Usuario):
    legajo = models.IntegerField(verbose_name="Legajo")
    rol = models.CharField(max_length=50, verbose_name="Rol")
    # cliente = models.ManyToManyField(Cliente, through="EmpleadoCliente", null=True)

    def __str__(self):
        return f"Empleado: {self.nombre_completo()} (Legajo: {self.legajo})"


class EmpleadoCliente(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

# Maestro de Materiales


class Material(models.Model):
    # Código único de material
    sku = models.CharField(verbose_name="SKU", unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)

    def __str__(self):
        return f'SKU: {self.sku} Descripcion: {self.descripcion}'

# Posiciones del depósito


class Posiciones(models.Model):
    posicion = models.CharField(verbose_name="Ubicación", max_length=10)
    estado = models.CharField(
        verbose_name="Estado de la posición", max_length=8, default="vacia")

    def __str__(self):
        return f'Posicion: {self.posicion} Estado: {self.estado}'


class Ingresos(models.Model):
    remito_fc = models.CharField(verbose_name="Remito/FC")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    materiales = models.ManyToManyField(Material, through="Stock")

    def __str__(self):
        return f'Remito / FC: {self.remito_fc} Fecha de Ingreso: {self.fecha_ingreso}'

    def mostrar_materiales(self):
        list_materiales = Stock.objects.filter(ingreso=self)
        return list_materiales

# Stock: Uniendo materiales y posiciones


class Stock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    posicion = models.ForeignKey(
        Posiciones, on_delete=models.CASCADE, default="stash")
    ingreso = models.ForeignKey(Ingresos, on_delete=models.CASCADE)

    def __str__(self):
        return f'Material: {self.material} Cantidad: {self.cantidad} {self.posicion} {self.ingreso}'

class Pedidos(models.Model):
    remito_OC = models.CharField(verbose_name="Remito / OC")
    fecha_pedido = fecha_pedido = models.DateField(verbose_name="Fecha del Pedido") 
    pedido_stock = models.ManyToManyField(Material, through="Salidas")

    def __str__(self):
        return f'Remito / OC: {self.remito_OC} Fecha del Pedido: {self.fecha_pedido}'
    
    def mostrar_materiales(self):
        list_materiales = Salidas.objects.filter(pedido=self)
        return list_materiales

class Salidas(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    del_stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
