from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("ingresos/", views.ingresos, name = "ingresos"),
    path("pedidos/", views.pedidos, name = "pedidos"),
    path("stock/", views.stock, name = "stock"),
    path("inventarios/", views.inventarios, name = "inventarios"),
    path("posiciones/", views.posiciones, name = "posiciones"),
    path("usuarios/", views.usuarios, name = "usuarios"),
    path("usuarios/<str:usuario_id>/", views.usuario_detalle, name = "usuario_detalle"),

]