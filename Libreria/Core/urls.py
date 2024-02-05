from django.urls import path
from Core import views

urlpatterns = [
    path('',views.home , name = 'Home'),
    path('libros/',views.libros, name ='Libros'),
    path('autor/',views.autor, name ='Autor'),
    path('clientes/',views.clientes, name ='Clientes'),
]