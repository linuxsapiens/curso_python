from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.response import Response
from rest_framework import status
from libros.models import Libro
from datetime import date

class APITestCase(TestCase):

    client = APIClient
    user   = User
    libro  = Libro
    respuesta = Response
    token  = None

    def setUp(self):
        self.client = APIClient()
        self.user   = User.objects.create_user(username="prueba3", password="PruebaPrueba")
        self.libro  = Libro.objects.create(
            titulo = 'Test Book',
            autor  = 'Test Author',
            isbn   = '1234567890',
            fecha_publicacion = date.today(),
            status = 'disponible',
        )

    def test_login(self):
        self.respuesta = self.client.post(
            '/api/auth/login/',
            {'username': 'prueba3', 'password': 'PruebaPrueba'}
        )
        self.assertEqual(self.respuesta.status_code, status.HTTP_200_OK)
        self.token = self.respuesta.json()
        self.assertIn('token', self.token)
        # print(f'token: {self.token}')

    def test_login_invalid_credentials(self):
        response = self.client.post(
            '/api/auth/login/', 
            {'username': 'testuser', 'password': 'wrongpass'},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_libros(self):
        self.test_login()
        libro = Libro.objects.filter(isbn__icontains='1234567890')[0]
        # print(f'libro: {libro.id} token: {self.token}')
        response = self.client.get(
            f'/api/libros/{libro.id}/',
            headers={"Authorization": f"token {self.token['token']}"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_resp = response.json()
        self.assertEqual(libro.id, json_resp['id'])

# Ejecutar usando: python manage.py test api

#    setUpClass: Happens before the FIRST test
#    setUp: Happens before EVERY test
#    tearDown: Happens after EVERY test
#    tearDownClass: Happens after the LAST test

