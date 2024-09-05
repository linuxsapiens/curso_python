from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha_devolucion']
        widgets = {
            'libro': forms.Select(attrs={'class': 'ui dropdown'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date', 'class': 'ui calendar'}),
        }