from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("logged_in/", views.logged_in, name="logged_in"),    
    path("listar_ingresos/", views.listar_ingresos, name = "listar_ingresos"),
    path("nuevo_ingreso/", views.nuevo_ingreso, name = "nuevo_ingreso"),
    path("modificar_ingreso/", views.modificar_ingreso, name = "modificar_ingreso"),
    path("pedidos/", views.pedidos, name = "pedidos"),
    path("stock/", views.stock, name = "stock"),
    path("inventarios/", views.inventarios, name = "inventarios"),
    path("posiciones/", views.posiciones, name = "posiciones"),
    path("usuarios/", views.usuarios, name = "usuarios"),
    path("alta_usuario/", views.alta_usuario, name="alta_usuario"),
    path('listado_usuarios/', views.listado_usuarios, name='listado_usuarios'),
    path("usuarios/<str:usuario_id>/", views.usuario_detalle, name = "usuario_detalle"),
]