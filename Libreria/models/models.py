from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 50)
    genero = models.CharField(max_length = 60)
    publicado = models.DateField()

    #metodo descriptivo
    def __str__(self):
        return self.titulo +'-'+ self.autor + '-' + self.publicado
    
    #ordenar
    class Meta:
        ordering = ['-titulo']

class Autor(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre  +'-' + self.apellido


class Clientes(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido =models.CharField(max_length = 50)
    email = models.EmailField()

