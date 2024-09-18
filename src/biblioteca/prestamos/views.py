from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import PrestamoForm, SolicitarPrestamoForm
from .models import Prestamo
from libros.models import Libro

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class PrestamoListView(AdminRequiredMixin, ListView):
    # if not user is_staff, redirect to home
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    model = Prestamo
    template_name = 'prestamo_list.html'
    context_object_name = 'prestamos'

class PrestamoCreateView(AdminRequiredMixin, CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PrestamoUpdateView(AdminRequiredMixin, UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoDeleteView(AdminRequiredMixin, DeleteView):
    model = Prestamo
    template_name = 'prestamo_confirm_delete.html'
    success_url = reverse_lazy('prestamo_list')

class SolicitarPrestamoView(LoginRequiredMixin, CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'solicitar_prestamo.html'
    success_url = reverse_lazy('prestamo_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

def solicitar_prestamo(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    
    if request.method == 'POST':
        form = SolicitarPrestamoForm(request.POST, libro=libro)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.libro = libro
            prestamo.usuario = request.user  # Asumiendo que tienes autenticación de usuario
            prestamo.save()
            return redirect('home')  # Asegúrate de tener esta URL definida
    else:
        form = SolicitarPrestamoForm(libro=libro)
    
    return render(request, 'solicitar_prestamo.html', {'form': form, 'libro': libro})

