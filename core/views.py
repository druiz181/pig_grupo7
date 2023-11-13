from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.urls import reverse
from .forms import IngresosForm, TipoUsuarioForm, ClienteForm, EmpleadoForm
from .models import Ingresos, Cliente, Empleado, Posiciones, Stock

user1 = {
    "dni": 111111111,
    "first_name": "User",
    "last_name": "Test",
    "email": "test@depotfy.com",
    "phone_number": 111111,
    "rol": "Warehouse Manager",
    "logged_in": True
}


users = [user1]
login_template = "core/account/login.html"


def logged_in(request):
    if request.POST['email'] == user1.get("email"):
        user = user1
        user["logged_in"] = True

        return render(request, "core/index.html",  context={"user1": user1})

    return render(request, login_template)


def index(request):
    if not user1["logged_in"]:
        return render(request, login_template)
    return render(request, "core/index.html", context={"user1": user1})


# Alta de materiales
@login_required
def nuevo_ingreso(request):
    if request.method == "POST":
        formulario = IngresosForm(request.POST)
        if formulario.is_valid():
            nuevo_ingreso = Ingresos(
                remito_fc=formulario.cleaned_data['remito_fc'],
                fecha_ingreso=formulario.cleaned_data['fecha_ingreso'],
                sku=formulario.cleaned_data['sku'],
                cantidad=formulario.cleaned_data['cantidad'],
            )
            try:
                nuevo_ingreso.save()
                messages.success(request, "Se registró el ingreso")
                return redirect("listar_ingresos")
            except IntegrityError as ie:
                messages.error(
                    request, "No se pudo registrar el ingreso debido a un error en la base de datos.")
    else:
        formulario = IngresosForm()

    context = {
        'nombre_usuario': 'Usuario de prueba',
        'nuevo_ingreso_form': formulario
    }
    return render(request, "core/nuevo_ingreso.html", context)

# Listado de ingresos


@login_required
def listar_ingresos(request):
    listado = Ingresos.objects.all().order_by('fecha_ingreso')
    context = {
        'listado_ingresos': listado,
        'nombre_usuario': 'Usuario de prueba',
    }
    return render(request, "core/listar_ingresos.html", context)


@login_required
def modificar_ingreso(request):

    context = {
        'nombre_usuario': 'Usuario de prueba',
    }

    return render(request, "core/modificar_ingreso.html", context)
    # if not user1["logged_in"]: return render(request, "core/accounts/login.html")


@login_required
def nuevo_pedido(request):
    if not user1["logged_in"]:
        return render(request, "core/login.html")

    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/nuevo_pedido.html", context)


@login_required
def listar_pedidos(request):
    if not user1["logged_in"]:
        return render(request, "core/login.html")

    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/listar_pedidos.html", context)


@login_required
def modificar_pedido(request):
    if not user1["logged_in"]:
        return render(request, "core/login.html")

    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/modificar_pedido.html", context)


@login_required
def listar_stock(request):
    listado = Stock.objects.all().order_by('posicion')
    context = {
        'listado_stock': listado,
        'nombre_usuario': 'Usuario de prueba',
    }
    return render(request, "core/listar_stock.html", context)


@login_required
def movimientos_material(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/movimientos_material.html", context)


@login_required
def inventarios(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/inventarios.html", context)


@login_required
def nueva_posicion(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/nueva_posicion.html", context)


@login_required
def listar_posiciones(request):
    listado = Posiciones.objects.all().order_by('posicion')
    context = {
        'listado_posiciones': listado,
        'nombre_usuario': 'Usuario de prueba',
    }
    return render(request, "core/listar_posiciones.html", context)


@login_required
def modificar_posicion(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/modificar_posicion.html", context)

# Usuarios


def usuarios(request):
    return render(request, 'core/usuarios.html', context={"user1": user1})


@login_required
def alta_usuario(request):
    if request.method == "POST":
        tipo_form = TipoUsuarioForm(request.POST)
        if tipo_form.is_valid():
            tipo_elegido = tipo_form.cleaned_data.get('tipo')
            if tipo_elegido == 'cliente':
                usuario_form = ClienteForm(request.POST)
            else:
                usuario_form = EmpleadoForm(request.POST)

            # Validación para que se elija el tipo
            if not tipo_elegido:
                tipo_form.add_error(
                    'tipo', 'Por favor, elija un tipo de usuario.')
            elif usuario_form.is_valid():
                usuario = usuario_form.save()
                return redirect('listado_usuarios')
            else:
                # Imprimir los errores en la consola
                print(usuario_form.errors)
    else:
        tipo_form = TipoUsuarioForm()
        usuario_form = None

    context = {
        'tipo_form': tipo_form,
        'usuario_form': usuario_form,
    }
    return render(request, 'core/alta_usuario.html', context)


@login_required
def listado_usuarios(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    context = {
        'clientes': clientes,
        'empleados': empleados,
    }
    return render(request, 'core/listado_usuarios.html', context)


@login_required
def usuario_detalle(request, usuario_id):
    return HttpResponse(f"Usuario Detalle {usuario_id}")
