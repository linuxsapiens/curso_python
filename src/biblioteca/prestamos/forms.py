from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha_devolucion', 'status', 'usuario']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'ui dropdown'}),
            'libro': forms.Select(attrs={'class': 'ui dropdown'}),
            'status': forms.Select(attrs={'class': 'ui dropdown'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date', 'class': 'ui calendar'}),
        }

class SolicitarPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_devolucion']
        widgets = {
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date', 'class': 'ui calendar'}),
        }

    def __init__(self, *args, **kwargs):
        self.libro = kwargs.pop('libro', None)
        super(SolicitarPrestamoForm, self).__init__(*args, **kwargs)
