from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("logged_in/", views.logged_in, name="logged_in"),
    path("listar_ingresos/", views.listar_ingresos, name="listar_ingresos"),
    path("nuevo_ingreso/", views.nuevo_ingreso, name="nuevo_ingreso"),
    path("modificar_ingreso/", views.modificar_ingreso, name="modificar_ingreso"),
    path("nuevo_pedido/", views.nuevo_pedido, name="nuevo_pedido"),
    path("listar_pedidos/", views.listar_pedidos, name="listar_pedidos"),
    path("modificar_pedido/", views.modificar_pedido, name="modificar_pedido"),
    path("listar_stock/", views.listar_stock, name="listar_stock"),
    path("movimientos_material/", views.movimientos_material,
         name="movimientos_material"),
    path("inventarios/", views.inventarios, name="inventarios"),
    path("nueva_posicion/", views.nueva_posicion, name="nueva_posicion"),
    path("modificar_posicion/", views.modificar_posicion,
         name="modificar_posicion"),
    path("listar_posiciones/", views.listar_posiciones, name="listar_posiciones"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("alta_usuario/", views.alta_usuario, name="alta_usuario"),
    path('listado_usuarios/', views.listado_usuarios, name='listado_usuarios'),
    path("usuarios/<str:usuario_id>/",
         views.usuario_detalle, name="usuario_detalle"),
]
