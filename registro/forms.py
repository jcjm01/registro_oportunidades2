from django import forms
from .models import Oportunidad

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_cierre_estimada', 'monto', 'productos','correo_electronico','numero_telefonico']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd', 'type': 'text'}),
            'fecha_cierre_estimada': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd', 'type': 'text'}),
            'productos': forms.CheckboxSelectMultiple(), 
            # Asegúrate de configurar otros campos según sea necesario
        }