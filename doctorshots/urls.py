from django.urls import path

from . import views

app_name = 'doctorshots'
urlpatterns = [
    path('', views.index, name='inicio'),
    #LOGIN
    path('formlogin/<str:mensaje>', views.formularioLogin, name= 'formlogin' ),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    #MODULO EMPLEADOS
    path('formempleado/<str:mensaje>', views.formularioEmpleados , name= 'formempleado'),
    path('guardarempleado', views.guardarEmpleado, name= 'guardarempleado'),
    path('editarempleado/<int:id>', views.formularioActualizarEmpleado, name= 'editarempleado' ),
    path('actualizarempleado', views.actualizarEmpleado, name= 'actualizarempleado'),
    path('crearempleadomovil',views.crearEmpleadoMovil, name='crearempleadomovil'),
    path('eliminarempleado/<int:id>', views.eliminarEmpleado, name='eliminarempleado'),
    #MODULO PRODUCTOS
    path('formproductos/<str:mensaje>', views.formularioProductos, name='formproductos'),
    path('guardarproducto', views.guardarProducto, name='guardarproducto'),
    path('verproducto/<int:id>', views.verProducto, name='verproducto'),
    path('crearproductomovil', views.crearProductoMovil, name='crearproductomovil'),
    path('formeditarproducto/<int:id>', views.formularioEditarProducto, name='formeditarproducto'),
    path('actualizarproducto', views.actualizarProducto , name='actualizarproducto'),
    path('eliminarproducto/<int:id>', views.eliminarProducto, name=('eliminarproducto')),
    path('crearcategoria', views.crearCategoria, name=('agregarcategoria')),
    #MODULO VENTAS
    path('ventas', views.formVentas, name=('formventas')),
    path('nuevamesa', views.formNuevaMesa, name=('nuevaMesa')),
    path('nuevaventa',views.nuevaVenta, name=('nuevaVenta')),
    path('listaprodcat/',views.listaprodcat, name='listaprodcat'),
    path('agregarproducto', views.agregarProducto, name='agregarproducto')

]
