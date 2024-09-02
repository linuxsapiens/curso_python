from django import forms
from .models import Libro

class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'fecha_publicacion', 'cover_image']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }