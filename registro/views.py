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
            # Lista de destinatarios
            destinatarios = ['carlos.jimenez@nephosit.com', 'juan_carlos_jimenez@outlook.com']
            send_mail(
                'Nueva Oportunidad Registrada',
                f'Se ha registrado una nueva oportunidad: {nueva_oportunidad.nombre}.',
                settings.EMAIL_HOST_USER,
                destinatarios,  # Usamos la lista de destinatarios aquí
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
    # Implementa tu lógica para seleccionar un producto. Esto es solo un placeholder.
    return render(request, 'registro/seleccionar_producto.html')
# Asegúrate de agregar o ajustar cualquier otra vista necesaria aquí
