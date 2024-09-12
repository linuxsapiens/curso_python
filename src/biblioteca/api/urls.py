from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, LoginViewSet, PrestamoViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'prestamos', PrestamoViewSet, basename='prestamos')
router.register(r'auth', LoginViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]