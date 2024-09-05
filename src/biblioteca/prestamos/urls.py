from django.urls import path
from .views import PrestamoListView, PrestamoCreateView, PrestamoUpdateView, PrestamoDeleteView

urlpatterns = [
    path('prestamos/', PrestamoListView.as_view(), name='prestamo_list'),
    path('prestamos/nuevo/', PrestamoCreateView.as_view(), name='prestamo_create'),
    path('prestamos/editar/<int:pk>/', PrestamoUpdateView.as_view(), name='prestamo_update'),
    path('prestamos/borrar/<int:pk>/', PrestamoDeleteView.as_view(), name='prestamo_delete'),
]