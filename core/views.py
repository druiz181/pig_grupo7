from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import IngresosForm

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

        return render(request, "core/index.html",  context={"user1":user1})
    
    return render(request, login_template)


def index(request):
    if not user1["logged_in"]: return render(request, login_template)
    return render(request, "core/index.html", context={"user1":user1})

def listar_ingresos(request):
    context = {
        'nombre_usuario': 'Usuario de prueba',
    }
    if not user1["logged_in"]: return render(request, "core/accounts/login.html")
    return render(request, "core/listar_ingresos.html", context)

def nuevo_ingreso(request):
    if request.method == "POST":
        formulario = IngresosForm(request.POST)
        if formulario.is_valid():
            return redirect("listar_ingresos")
    else:
        formulario = IngresosForm()
    context = {
        'nombre_usuario': 'Usuario de prueba',
        'nuevo_ingreso_form' : formulario
    }
    return render(request, "core/nuevo_ingreso.html", context)

def modificar_ingreso(request):
    context = {
        'nombre_usuario': 'Usuario de prueba',
    }
    if not user1["logged_in"]: return render(request, "core/accounts/login.html")
    return render(request, "core/modificar_ingreso.html", context)

def pedidos(request):
    if not user1["logged_in"]: return render(request, "core/login.html")

    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/pedidos.html", context)

def stock(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/stock.html", context)

def inventarios(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/inventarios.html", context)

def posiciones(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/posiciones.html", context)

def usuarios(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/usuarios.html", context)

def usuario_detalle(request, usuario_id):
    return HttpResponse(f"Usuario Detalle {usuario_id}")

