from django.shortcuts import render,HttpResponse
#import formularios
from api.forms import Libro_formulario
#import models
from models.models import Libro
#view inicio 
def home(request):
    return render(request, 'Core/inicio.html')
#view de libros con su genero
def libros(request):
    #creando formulario
    if request.method == 'POST':
        
        libroForm = Libro_formulario(request.POST)
        print(libroForm)
        
        #si el formulario es valido =>
        if libroForm.is_valid():
            
            #crear formulario vacio
            info = libroForm.cleaned_data
            
            libro = Libro(Nombre = info['nombre'], Autor = info['autor'], Genero = info['genero'])
            #guardamos el objeto
            libro.save()
            #vuelvo al inicio
            return render(request, 'Core/inicio.html')
    else:
        #formulario vacio
        libroForm = Libro_formulario()
        
    #retornamos donde queremos ir y le pasamos el diccionario(form)
    return render(request, "Core/libros.html", {"libroForm":libroForm})
#-----------------------------------------------------------------------------------------------------------#



#view autores
def autor(request):
    return render(request, 'Core/autor.html')

#view de clientes (datos)
def clientes(request):
    return render(request, 'Core/clientes.html')

#view de contacto
def contacto(request):
    return render(request, 'Core/contacto.html')

