from django.db import models

class Categoria(models.Model):
    descripcion = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    titulo       = models.CharField(max_length=500, null=False)
    imagen       = models.ImageField(upload_to='imagenes/')
    descripcion  = models.CharField(max_length=2500, null=False)
    precio       = models.DecimalField(decimal_places=2, max_digits=50, default=0.00)
    categoria    = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

