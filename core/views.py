from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

user1 = {
    "dni": 111111111,
    "first_name": "Javier",
    "last_name": "Milei",
    "email": "javicho@gmail.com",
    "phone_number": 111111,
    "rol": "Warehouse Manager",
    "logged_in": False
}
user2 = {
    "dni": 111111111,
    "first_name": "Donald",
    "last_name": "Trump",
    "email": "el_peluca@gmail.com",
    "phone_number": 111111,
    "rol": "Invetory Manager",
    "logged_in": False
}

users = [user1, user2]

def logged_in(request):
    # if request.POST['email'] in [user.get("email") for user in users]:
        # user = list(filter(lambda u: (u["email"] == request.POST['email']), users))[0]
    if request.POST['email'] == user1.get("email"):
        user = user1
        user["logged_in"] = True

        return render(request, "core/index.html",  context={"user1":user1})
    
    return render(request, "core/login.html")


def index(request):
    # if args == {}: return render(request, "core/login.html")
    if not user1["logged_in"]: return render(request, "core/login.html") 
    # context = user1
    return render(request, "core/index.html", context={"user1":user1})

# def ingresos(request):
#     return HttpResponse("Ingresos")

# def pedidos(request):
#     return HttpResponse("Pedidos")

# def stock(request):
#     return HttpResponse("Stock")

# def inventarios(request):
#     return HttpResponse("Inventarios")

# def posiciones(request):
#     return HttpResponse("Posiciones")

# def usuarios(request):
#     return HttpResponse("Usuarios")

# def usuario_detalle(request, usuario_id):
#     return HttpResponse(f"Usuario Detalle {usuario_id}")

