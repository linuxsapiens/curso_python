from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.book_list, name='book_list'),
    path('libros/<int:pk>/', views.book_detail, name='book_detail'),
    path('libros/create/', views.BookCreate.as_view(), name='book_create'),
    path('libros/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('libros/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('libros/add_books_from_api/', views.add_books_from_api, name='add_books_from_api'),
    path('libros/buscar/', views.buscar_libros, name='buscar_libros'),
]