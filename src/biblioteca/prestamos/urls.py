from django.urls import path
from .views import PrestamoListView, PrestamoCreateView, PrestamoUpdateView, PrestamoDeleteView, SolicitarPrestamoView
from . import views

urlpatterns = [
    path('prestamos/', PrestamoListView.as_view(), name='prestamo_list'),
    path('prestamos/nuevo/', PrestamoCreateView.as_view(), name='prestamo_create'),
    path('prestamos/editar/<int:pk>/', PrestamoUpdateView.as_view(), name='prestamo_update'),
    path('prestamos/borrar/<int:pk>/', PrestamoDeleteView.as_view(), name='prestamo_delete'),
    path('prestamos/solicitar/<int:pk>/', SolicitarPrestamoView.as_view(), name='solicitar_prestamo'),
    path('solicitar-prestamo/<int:libro_id>/', views.solicitar_prestamo, name='solicitar_prestamo'),
]