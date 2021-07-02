from django.shortcuts import render
from .models import Categoria, Producto #importo las clases de models, tanto de producto como de categoria

# Create your views here.
def index(request):
    variableProducto = Producto.objects.all()[0:3] #genero la variable "variableProducto" y me traigo todo (all) lo que tengo en la clase producto
    variableProducto2 = Producto.objects.all()[3:10]
    return render(request, "index.html", {
        'variableProducto':variableProducto,
        'variableProducto2':variableProducto2,})