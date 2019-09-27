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
    path('crearempleadomovil',views.crearEmpleadoMovil, name='crearempleadomovil')
]
