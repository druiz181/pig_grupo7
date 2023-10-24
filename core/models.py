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

    empresa = models.CharField(max_length = 50, verbose_name="Empresa", null=True)

class Empleado(Usuario): 
    legajo = models.IntegerField(verbose_name="Legajo")
    rol = models.CharField(max_length = 50, verbose_name="Rol")
    #cliente = models.ManyToManyField(Cliente, through="EmpleadoCliente", null=True)
    
    def __str__(self):
        return f"Empleado: {self.nombre_completo()} (Legajo: {self.legajo})"

 
class EmpleadoCliente(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Materiales(models.Model):
    remito_fc = models.CharField(verbose_name="Remito/FC")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    sku = models.CharField(verbose_name="SKU", unique=True) #Código único de material
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad") #No se puede ingresar < 1

    def __str__(self):
        return self.descripcion

#Posiciones del depósito
class Posiciones(models.Model):
    pass
    # ubicacion = models.CharField(verbose_name="Ubicación", max_length=10) 
    # estado = models.CharField(verbose_name="Estado de la posición", max_length=8)

#Stock: Uniendo materiales, clientes y posiciones
class Stock(models.Model):
    pass


