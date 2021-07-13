from django.shortcuts import get_object_or_404, render
from .models import Categoria, Producto #importo las clases de models, tanto de producto como de categoria
from django.db.models import Q
from django.views.generic.list import ListView

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
def producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "producto.html", {
        'producto': producto,
     })


class search(ListView):
    model = Producto
    template_name = 'search.html'
        
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Producto.objects.filter( #va a filtrar segun:
             Q(titulo__icontains=query) | #aca indico que quiero buscar por titulo y por descripcion. Podria agregar mas, pero es lo que pide en el trabajo
             Q(descripcion__icontains=query) |
             Q(categoria__descripcion__icontains=query)
        )
        return object_list 
