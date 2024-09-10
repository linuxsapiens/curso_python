from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from datetime import date
from .models import Libro
from .forms import BookForm, BookSearchForm
from .utils import search_books, download_book_cover
from django.core.paginator import Paginator
from django.db.models import Q

def book_list(request):
    books = Libro.objects.all()
    return render(request, 'list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Libro, pk=pk)
    return render(request, 'detail.html', {'book': book})

class BookCreate(CreateView):
    model = Libro
    form_class = BookForm
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Libro
    form_class = BookForm
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Libro
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book_list')


def add_books_from_api(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books_data = search_books(query)
            
            for book_data in books_data:
                # check if the book already exists in the database
                if Libro.objects.filter(isbn=book_data['isbn']).exists():
                    print(f"El libro {book_data['title']} ya existe en la base de datos")
                    continue
                # if missing url cover, continue
                if not book_data['cover_image_url'] or book_data['cover_image_url'] == "":
                    print(f"El libro {book_data['title']} no tiene URL de imagen")
                    continue
                
                Libro.objects.create(
                    titulo=book_data['title'],
                    autor=book_data['author'],
                    isbn=book_data['isbn'],
                    fecha_publicacion=book_data['published_date'] if 'published_date' and book_data['published_date'] != None else date.today(),
                    cover_image=download_book_cover(book_data['cover_image_url'])
                )
            
            return redirect('book_list')  # Asume que tienes una vista llamada 'book_list'
    else:
        form = BookSearchForm()
    
    return render(request, 'add_books_from_api.html', {'form': form})

def buscar_libros(request):
    query = request.GET.get('q')
    page_number = request.GET.get('page', 1)
    
    if query and query != "" and query != " " and query != None:
        libros = Libro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(isbn__icontains=query)
        )
    else:
        libros = Libro.objects.all()
    
    paginator = Paginator(libros, 10)  # 10 libros por página
    page_obj = paginator.get_page(page_number)
    if query:
        return render(request, 'buscar_libros.html', {'page_obj': page_obj, 'query': query})
    else:
        return render(request, 'buscar_libros.html', {'page_obj': page_obj})