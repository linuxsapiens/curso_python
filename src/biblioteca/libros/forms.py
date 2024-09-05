from django import forms
from .models import Libro

class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'fecha_publicacion', 'cover_image']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'ui input'}),
            'autor': forms.TextInput(attrs={'class': 'ui input'}),
            'isbn': forms.TextInput(attrs={'class': 'ui input'}),
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date', 'class': 'ui calendar'}),
            'cover_image': forms.FileInput(attrs={'class': 'ui file input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'field'})