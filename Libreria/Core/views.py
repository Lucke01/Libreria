from django.shortcuts import render,HttpResponse


#view inicio 
def home(request):
    return HttpResponse('''
                        <title> Inicio </title>
                        <h1> inicio </h1>''')

#view de libros con su genero
def libros(request):
    return HttpResponse('''
                        <title> libros </title>
                        <h1> Libros </h1>''')

#view autores
def autor(reauest):
    return HttpResponse('''
                        <title> autor </title>
                        <h1> autor </h1>''')

#view de clientes (datos)
def clientes(request):
    return HttpResponse('''
                        <title> clientes </title>
                        <h1> clientes </h1>''')


