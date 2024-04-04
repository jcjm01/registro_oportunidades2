from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Producto, Oportunidad
from .forms import OportunidadForm

def crear_oportunidad(request):
    if request.method == 'POST':
        form = OportunidadForm(request.POST)
        if form.is_valid():
            nueva_oportunidad = form.save()
            
            # Prepara el contenido del correo incluyendo los nombres de los productos seleccionados
            nombres_productos = [producto.nombre for producto in nueva_oportunidad.productos.all()]
            contenido_correo = (
                f"Nombre: {nueva_oportunidad.nombre}\n"
                f"Descripción: {nueva_oportunidad.descripcion}\n"
                f"Fecha de Inicio: {nueva_oportunidad.fecha_inicio}\n"
                f"Fecha de Cierre Estimada: {nueva_oportunidad.fecha_cierre_estimada}\n"
                f"Monto: {nueva_oportunidad.monto}\n"
                f"Correo Electrónico: {nueva_oportunidad.correo_electronico}\n"
                f"Número Telefónico: {nueva_oportunidad.numero_telefonico}\n"
                f"Productos: {', '.join(nombres_productos)}"
            )

            send_mail(
                'Nueva Oportunidad Registrada',
                contenido_correo,
                settings.EMAIL_HOST_USER,
                ['carlos.jimenez@nephosit.com','juan_carlos_jimenez@outlook.com'],  # Reemplaza con los correos reales de los destinatarios
                fail_silently=False,
            )
            return redirect('gracias')
    else:
        form = OportunidadForm()
    return render(request, 'registro/crear_oportunidad.html', {'form': form})

def gracias(request):
    # Vista para mostrar una página de agradecimiento
    return render(request, 'registro/gracias.html')

def listar_productos(request):
    # Vista para listar productos
    productos = Producto.objects.all()
    return render(request, 'registro/listar_productos.html', {'productos': productos})

def seleccionar_producto(request):
    # Esto es solo un placeholder. Deberás implementar la lógica específica si necesitas esta vista.
    return render(request, 'registro/seleccionar_producto.html')
