from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from datetime import date
from .models import Libro
from .forms import BookForm, BookSearchForm
from .utils import search_books, download_book_cover
from django.core.paginator import Paginator
from django.db.models import Q
import json
from django.core.serializers.json import DjangoJSONEncoder
# from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

def es_admin(user):
    return user.is_authenticated and user.is_staff

def admin_required(view_func):
    decorated_view_func = user_passes_test(es_admin, login_url='login')(view_func)
    def wrapper(request, *args, **kwargs):
        if not es_admin(request.user):
            return redirect('home')  # O donde quieras redirigir a los no administradores
        return decorated_view_func(request, *args, **kwargs)
    return wrapper

@admin_required
def book_list(request):
    libros = Libro.objects.all().order_by('titulo')
    paginator = Paginator(libros, 10)  # 10 libros por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'list.html', {'page_obj': page_obj})

@admin_required
def book_detail(request, pk):
    book = get_object_or_404(Libro, pk=pk)
    return render(request, 'detail.html', {'book': book})

class BookCreate(AdminRequiredMixin, CreateView):
    model = Libro
    form_class = BookForm
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')

class BookUpdate(AdminRequiredMixin, UpdateView):
    model = Libro
    form_class = BookForm
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')

class BookDelete(AdminRequiredMixin, DeleteView):
    model = Libro
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book_list')

@admin_required
def search_books_from_api(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books_data = search_books(query)
            for index, book in enumerate(books_data):
                book['id'] = index  # Añadimos un id único a cada libro
            request.session['search_results'] = json.dumps(books_data, cls=DjangoJSONEncoder)
            return render(request, 'select_books.html', {'books': books_data})
    else:
        form = BookSearchForm()
    
    return render(request, 'search_books_from_api.html', {'form': form})

@admin_required
def add_selected_books(request):
    if request.method == 'POST':
        selected_book_ids = request.POST.getlist('selected_books')
        search_results = json.loads(request.session.get('search_results', '[]'))
        for book_id in selected_book_ids:
            book_data = next((book for book in search_results if book['id'] == int(book_id)), None)
            if book_data and not Libro.objects.filter(isbn=book_data['isbn']).exists():
                if book_data['cover_image_url']:
                    Libro.objects.create(
                        titulo=book_data['title'],
                        autor=book_data['author'],
                        isbn=book_data['isbn'],
                        fecha_publicacion=book_data.get('published_date') or date.today(),
                        cover_image=download_book_cover(book_data['cover_image_url'])
                    )
        del request.session['search_results']  # Limpiamos los resultados de la sesión
        return redirect('book_list')
    return redirect('search_books_from_api')

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