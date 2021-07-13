from django.urls import path
from . import views
from .views import search 
app_name = "tienda"

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca', views.acerca, name="acerca"),
    path('search', search.as_view(), name="search"), #cuando es nombre . as_view(), es porque es una clase
    path('producto/<int:producto_id>', views.producto, name="producto") #cuando es views . nombre, es porque es una funcion
] 

