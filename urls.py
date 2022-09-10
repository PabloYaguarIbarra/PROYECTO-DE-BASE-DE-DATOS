from django.urls import path

from . import views

urlpatterns = [
    path('',views.Inicio,name="Inicio"),
    path('tipocarne',views.TipoCarne,name='tipocarne'),
    path('agregar',views.agregar,name='agregar'),
    path('editar/<str:id_tipocarne>',views.editar,name='editar'),
    path('update',views.update,name='update'),
    path('borrar/<str:id_tipocarne>',views.borrar,name='borrar'),

    path('producto',views.Prod,name='producto'),    
    path('agregarprod',views.agregarprod,name='agregarprod'),
    path('editarprod/<str:id_producto>',views.editarprod,name='agregarprod'),
    path('updateprod',views.updateprod,name='updateprod'),
    path('borrarprod/<str:id_producto>',views.borrarprod,name='borrarprod'),

    path('direccion',views.Direcciones,name='direccion'),
    path('agregardir',views.agregardir,name='agregardir'),
    path('editardir/<str:id_direccion>',views.editardir,name='editardir'),
    path('updatedir',views.updatedir,name='updatedir'),
    path('borrardir/<str:id_direccion>',views.borrardir,name='borrardir'),

    path('factura',views.Factu,name='factura'),
    path('agregarfac',views.agregarfac,name='agregarfac'),
    path('editarfac/<str:numfac>',views.editarfac,name='editarfac'),
    path('updatefac',views.updatefac,name='updatefac'),
    path('borrarfac/<str:numfac>',views.borrarfac,name='borrarfac'),

    path('proveedor',views.Prove,name='proveedor'),
    path('agregarprove',views.agregarprove,name='agregarprove'),
    path('editarprove/<str:cod_proveedor>',views.editarprove,name='editarprove'),
    path('updateprove',views.updateprove,name='updateprove'),
    path('borrarprove/<str:cod_proveedor>',views.borrarprove,name='borrarprove'),    
]

    