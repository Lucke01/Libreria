#impoetamos formularios

from django import forms



#formulario Libro
class Libro_formulario(forms.Form):
    #def los campos del formulario
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()