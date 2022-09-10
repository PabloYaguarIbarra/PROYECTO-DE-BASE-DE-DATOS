
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Tipo_Carne(models.Model):
    id_tipocarne = models.CharField(primary_key=True,max_length=6)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.id_tipocarne, self.descripcion)

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=6)
    id_tipocarne = models.ForeignKey(Tipo_Carne, on_delete=models.CASCADE)
    corte = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.id_producto, self.corte)
 
class Direccion(models.Model):
    id_direccion = models.CharField(primary_key=True, max_length=6)
    direccion = models.CharField(max_length=50)
    
    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.id_direccion, self.direccion)


class Factura(models.Model):
    numfac = models.CharField(primary_key=True, max_length=6)
    fecha = models.DateField()

    def __str__(self):
        txt = "{0}"
        return txt.format(self.numfac)

class Proveedor(models.Model):
    cod_proveedor = models.CharField(primary_key=True, max_length=6)
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10 )
    correo = models.EmailField(max_length=50)

    def __str__(self):
        txt = "{0} ({'1'})"
        return txt.format(self.cod_proveedor,self.nombre)

