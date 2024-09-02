from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Libro
from .forms import BookForm

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
