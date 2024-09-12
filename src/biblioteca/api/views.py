from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login
from libros.models import Libro
from .serializers import LibroSerializer, LoginSerializer, PrestamoSerializer
from libros.utils import search_books
from prestamos.models import Prestamo

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    @action(detail=False, methods=['post'])
    def add_books_from_api(self, request):
        query = request.data.get('query')
        if not query:
            return Response({"error": "Se requiere un parámetro 'query'"}, status=400)

        books_data = search_books(query)
        process_books_data(books_data)

        return Response({"message": f"Se procesaron {len(books_data)} libros"})

class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prestamo.objects.filter(usuario=self.request.user)
