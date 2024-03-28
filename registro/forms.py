from django import forms
from .models import Oportunidad

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_cierre_estimada', 'monto', 'producto']
