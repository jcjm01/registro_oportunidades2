from django import forms
from .models import Oportunidad

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_cierre_estimada', 'monto', 'productos', 'correo_electronico', 'numero_telefonico']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd', 'type': 'text'}),
            'fecha_cierre_estimada': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd', 'type': 'text'}),
            # Actualizar el campo 'productos' para usar Select2
            'productos': forms.SelectMultiple(attrs={'class': 'select2', 'style': 'width: 100%'}),
            # Nota: Se ha cambiado de CheckboxSelectMultiple a SelectMultiple
            # y se ha añadido la clase 'select2' para la inicialización de Select2
        }
