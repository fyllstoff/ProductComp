# productos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Vista principal
    path('register/', views.register, name='register'),  # Registro de usuario
    path('login/', views.login_view, name='login'),  # Inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # Cierre de sesión
    path('listar/', views.listar_productos, name='listar_productos'),  # Listar productos
    path('registrar/', views.registrar_producto, name='registrar_producto'),  # Registrar producto
    path('insertar/', views.insertar_producto, name='insertar_producto'),  # Insertar producto
    path('actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),  # Actualizar producto
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar producto
]
