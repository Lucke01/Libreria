from django.shortcuts import render,HttpResponse


#view inicio 
def home(request):
    return render(request, 'Core/inicio.html')
#view de libros con su genero
def libros(request):
    return render(request, 'Core/libros.html')

#view autores
def autor(request):
    return render(request, 'Core/autor.html')

#view de clientes (datos)
def clientes(request):
    return render(request, 'Core/clientes.html')

#view de contacto
def contacto(request):
    return render(request, 'Core/contacto.html')

