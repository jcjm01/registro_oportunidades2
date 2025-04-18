from django.contrib import admin
from .models import Producto, Oportunidad  # Asegúrate de importar tus modelos aquí

# Configuración de administración para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'en_stock')  # Ajusta estos campos según tu modelo Producto
    list_filter = ('en_stock',)  # Ejemplo de filtro por el campo en_stock
    #search_fields = ('nombre', 'descripcion')  # Habilita la búsqueda por nombre y descripción

# Registra el modelo Producto con la configuración de ProductoAdmin
admin.site.register(Producto, ProductoAdmin)

# Configuración de administración para Oportunidad (si es aplicable)
class OportunidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_cierre_estimada', 'monto', 'mostrar_productos')  # Ajusta según tu modelo Oportunidad y añade 'mostrar_productos'
    list_filter = ('fecha_inicio', 'fecha_cierre_estimada')  # Ejemplo de filtros
    search_fields = ('nombre', 'descripcion')  # Habilita la búsqueda por nombre y descripción

    def mostrar_productos(self, obj):
      return ", ".join ([producto.nombre for producto in obj.productos.all()])
    mostrar_productos.short_description = "Productos Asociados"

# Registra el modelo Oportunidad con la configuración de OportunidadAdmin
admin.site.register(Oportunidad, OportunidadAdmin)
