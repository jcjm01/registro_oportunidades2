# En tu archivo registro/urls.py

from django.urls import path
from . import views  # Importa correctamente todas las vistas como 'views'

urlpatterns = [
    path('crear/', views.crear_oportunidad, name='crear_oportunidad'),  # Usa views.crear_oportunidad
    path('gracias/', views.gracias, name='gracias'),  # Usa views.gracias
    path('seleccionar-producto/', views.seleccionar_producto, name='seleccionar_producto'),
    path('productos/', views.listar_productos, name='listar_productos'),

]
