from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Prestamo
from .forms import PrestamoForm
from django.shortcuts import redirect

class PrestamoListView(LoginRequiredMixin, ListView):
    # if not user is_staff, redirect to home
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    model = Prestamo
    template_name = 'prestamo_list.html'
    context_object_name = 'prestamos'

class PrestamoCreateView(LoginRequiredMixin, CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PrestamoUpdateView(LoginRequiredMixin, UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoDeleteView(LoginRequiredMixin, DeleteView):
    model = Prestamo
    template_name = 'prestamo_confirm_delete.html'
    success_url = reverse_lazy('prestamo_list')
