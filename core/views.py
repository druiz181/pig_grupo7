from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/index.html", context)

def ingresos(request):
    context = {'nombre_usuario': 'Usuario de prueba'}
    return render(request, "core/ingresos.html", context)

def pedidos(request):
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

