from django.shortcuts import render
from .models import Categoria, Producto #importo las clases de models, tanto de producto como de categoria

# Create your views here.
def index(request):
    variableProducto = Producto.objects.all()[0:3] #genero la variable "variableProducto" y me traigo todo (all) lo que tengo en la clase producto
    variableProducto2 = Producto.objects.all()[3:10]
    variableCategoria1 = Categoria.objects.all() 
    return render(request, "index.html", {
        'variableProducto':variableProducto,
        'variableProducto2':variableProducto2,
        'variableCategoria1':variableCategoria1,}) 
def navbar(request):   
    variableCategoria1 = Categoria.objects.all() 
    return render(request, "layout/navbar.html", {
        'variableCategoria1':variableCategoria1,}) 
def acerca(request):
    variableCategoria1 = Categoria.objects.all() 
    return render(request, "acerca.html", {
        'variableCategoria1':variableCategoria1,
    })
