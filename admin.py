from atexit import register
from math import factorial
from django.contrib import admin
from . models import Tipo_Carne, Producto, Direccion, Factura, Proveedor

# Register your models here.
admin.site.register(Tipo_Carne)
admin.site.register(Producto)
admin.site.register(Direccion)
admin.site.register(Factura)
admin.site.register(Proveedor)