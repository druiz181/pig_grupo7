from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index")

def ingresos(request):
    return HttpResponse("Ingresos")

def pedidos(request):
    return HttpResponse("Pedidos")

def stock(request):
    return HttpResponse("Stock")

def inventarios(request):
    return HttpResponse("Inventarios")

def posiciones(request):
    return HttpResponse("Posiciones")

def usuarios(request):
    return HttpResponse("Usuarios")

def usuario_detalle(request, usuario_id):
    return HttpResponse(f"Usuario Detalle {usuario_id}")

