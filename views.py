from math import fabs
from django.shortcuts import render, redirect
from .models import Factura, Proveedor, Tipo_Carne, Producto, Direccion

# Create your views here.

def Inicio(request):
    return render(request, 'Inicio.html')

def TipoCarne(request):
    listatipocarne = Tipo_Carne.objects.all()
    return render(request,'tipocarne.html', {"tipocarne":listatipocarne})

def agregar(request):
    id_tipocarne=request.POST['txtid_tipocarne']
    descripcion=request.POST['txtdescripcion']

    agregar = Tipo_Carne.objects.create(id_tipocarne=id_tipocarne, descripcion=descripcion)
    return redirect('tipocarne')

def editar(request, id_tipocarne):
    editar = Tipo_Carne.objects.get(id_tipocarne=id_tipocarne)
    return render(request, 'Edicion.html', {'editar':editar})

def update(request):
    id_tipocarne=request.POST['txtid_tipocarne']
    descripcion=request.POST['txtdescripcion']

    editar = Tipo_Carne.objects.get(id_tipocarne=id_tipocarne)
    
    editar.id_tipocarne = id_tipocarne
    editar.descripcion = descripcion
    editar.save()
    return redirect('tipocarne')

def borrar(request,id_tipocarne):
    borrar = Tipo_Carne.objects.get(id_tipocarne=id_tipocarne)
    borrar.delete()
    return redirect('tipocarne')



def Prod(request):
    listaprod = Producto.objects.all()
    return render(request,'Producto.html', {"listaprod":listaprod})

def agregarprod(request):
    id_producto=request.POST['txtid_producto']
    corte=request.POST['txtcorte']
    precio=request.POST['txtprecio']

    agregarprod = Producto.objects.create(id_producto=id_producto, corte=corte,precio=precio)
    return redirect('producto')

def editarprod(request, id_producto):
    editarprod = Producto.objects.get(id_producto=id_producto)
    return render(request, 'Ediprod.html', {'editarprod':editarprod})
    
def updateprod(request):
    id_producto=request.POST['txtid_producto']
    corte=request.POST['txtcorte']
    precio=request.POST['txtprecio']

    editar = Producto.objects.get(id_producto=id_producto)
    
    editar.id_producto = id_producto
    editar.corte = corte
    editar.precio = precio
    editar.save()
    return redirect('producto')

def borrarprod(request,id_producto):
    borrar = Producto.objects.get(id_producto=id_producto)
    borrar.delete()
    return redirect('producto')


def Direcciones(request):
    listadireccion = Direccion.objects.all()
    return render(request,'direccion.html', {"listadireccion":listadireccion})

def agregardir(request):
    id_direccion=request.POST['txtid_direccion']
    direccion=request.POST['txtdireccion']
    
    agregardir = Direccion.objects.create(id_direccion=id_direccion, direccion=direccion)
    return redirect('direccion')

def editardir(request, id_direccion):
    editardir = Direccion.objects.get(id_direccion=id_direccion)
    return render(request, 'Edidir.html', {'editardir':editardir})

def updatedir(request):
    id_direccion=request.POST['txtid_direccion']
    direccion=request.POST['txtdireccion']
    
    editardir = Direccion.objects.get(id_direccion=id_direccion)
    
    editardir.id_direccion = id_direccion
    editardir.direccion = direccion
    editardir.save()
    return redirect('direccion')

def borrardir(request,id_direccion):
    borrar = Direccion.objects.get(id_direccion=id_direccion)
    borrar.delete()
    return redirect('direccion')



def Factu(request):
    listafactu = Factura.objects.all()
    return render(request,'factura.html', {"listafactu":listafactu})

def agregarfac(request):
    numfac=request.POST['txtnumfac']
    fecha=request.POST['txtfecha']
    
    agregarfac = Factura.objects.create(numfac=numfac, fecha=fecha)
    return redirect('factura')

def editarfac(request, numfac):
    editarfac = Factura.objects.get(numfac=numfac)
    return render(request, 'Edifac.html', {'editarfac':editarfac})

def updatefac(request):
    numfac=request.POST['txtnumfac']
    fecha=request.POST['txtfecha']
    
    editarfac = Factura.objects.get(numfac=numfac)
    
    editarfac.numfac = numfac
    editarfac.fecha = fecha
    editarfac.save()
    return redirect('factura')

def borrarfac(request,numfac):
    borrar = Factura.objects.get(numfac=numfac)
    borrar.delete()
    return redirect('factura')


def Prove(request):
    listaprove = Proveedor.objects.all()
    return render(request,'proveedor.html', {"listaprove":listaprove})

def agregarprove(request):
    cod_proveedor=request.POST['txtcod_proveedor']
    ruc=request.POST['txtruc']
    nombre=request.POST['txtnombre']
    telefono=request.POST['txttelefono']
    correo=request.POST['txtcorreo']
    
    agregarfac = Proveedor.objects.create(cod_proveedor=cod_proveedor, ruc=ruc,nombre=nombre,telefono=telefono,correo=correo )
    return redirect('proveedor')

def editarprove(request, cod_proveedor):
    editarprove = Proveedor.objects.get(cod_proveedor=cod_proveedor)
    return render(request, 'Ediprove.html', {'editarprove':editarprove})

def updateprove(request):
    cod_proveedor=request.POST['txtcod_proveedor']
    ruc=request.POST['txtruc']
    nombre=request.POST['txtnombre']
    telefono=request.POST['txttelefono']
    correo=request.POST['txtcorreo']
    
    editarprove = Proveedor.objects.get(cod_proveedor=cod_proveedor)
    
    editarprove.cod_proveedor = cod_proveedor
    editarprove.ruc = ruc
    editarprove.nombre = nombre
    editarprove.telefono = telefono
    editarprove.correo = correo
    editarprove.save()
    return redirect('proveedor')

def borrarprove(request,cod_proveedor):
    borrar = Proveedor.objects.get(cod_proveedor=cod_proveedor)
    borrar.delete()
    return redirect('proveedor')