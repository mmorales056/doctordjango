from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.forms.models import model_to_dict
from doctorshots.models import Usuarios,Productos, CategoriaProducto

# Create your views here.
'''inicio'''
# Este metodo se encarga de pintarme redireccionarme al index   
def index(request):
    return render(request,'doctorshots/index.html')

'''login'''
# Este metodo se encarga de pintarme redireccionarme al fornmulario login        
def formularioLogin(request,mensaje):
    contexto = {'mensaje':mensaje }
    return render(request,'doctorshots/formulario-login.html',contexto)
#Este metodo se encarga de hacer el login y construir variable de session
def login(request):
    try:
        usuario = request.POST['usuario']
        password = request.POST['clave']
        q= Usuarios.objects.get(usuario = usuario)
        if q.clave == password:
            request.session['logueado'] = [q.cedula, q.nombres, q.clave, q.Rol ]
            return render(request,'doctorshots/index.html')
        else:
            return HttpResponseRedirect(reverse ('doctorshots:formlogin',args=('password invalid',)))
                                                
    except Exception as e:
        #return HttpResponseRedirect(reverse ('doctorshots:formlogin',args=(e,)))
        return HttpResponse(e)
#Este metodo se encarga de cerrar la session
def logout(request):
    try:
        del request.session['logueado']
        return render(request, 'doctorshots/index.html')
    
    except Exception as e:
        return render(request, 'doctorshots/index.html')

'''Empleados'''
#Este metodo se encarga de mostrar el html formulario de empleado
def formularioEmpleados(request, mensaje):
    try:
        ses = request.session.get('logueado',False)
        if ses and ses[3]=='2':
            q= Usuarios.objects.all()
            contexto = {'datos': q, 'mensaje': mensaje }
            return render(request,'doctorshots/form-crear-empleado.html',contexto)
        else:
            contexto = {'s':'fallo'}
            return  render(request,'doctorshots/index.html',contexto)
        
    except Exception as e:
        return HttpResponse(e)
# Este metodo Guarda un empleado
def guardarEmpleado(request):
   try:
       ses = request.session.get('logueado',False)
       if ses and ses[3]=='2':
           empleado = Usuarios(
               cedula = request.POST['cedula'],
               nombres= request.POST['nombres'],
               usuario = request.POST['usuario'],
               clave = request.POST['clave'],
               Rol = '1'
            )
           empleado.save()
           return HttpResponseRedirect(reverse ('doctorshots:formempleado' ,args=('GuardadoCorrectamente',)))
       else:           
           return render(request,'doctorshots/index.html',{'s':'fallo'})
   
   except Exception as e:
       return HttpResponseRedirect(reverse ('doctorshots:formempleado' ,args=(e,)))
#Este metodo se encarga de cargarme el template para actualizar el empleado desde un escritorio
def formularioActualizarEmpleado(request,id):
    try:
        q = Usuarios.objects.get(pk=id)
        contexto = {'empleado': q}
        return render(request,'doctorshots/form-editar-empleado.html',contexto)
    except Exception as e:
        return HttpResponse(e)
#Este metodo se encarga de cargarme el template para actualizar el empleado
def actualizarEmpleado(requuest):
    try:
        id = request.POST['id']
        q = Usuarios.objects.get(pk=id)
        q.cedula= request.POST['cedula']
        q.nombres= request.POST['nombres']
        q.usuario= request.POST['usuario']
        q.clave= request.POST['clave']        
        q.save()
        return HttpResponseRedirect(reverse('doctorshots:formempleado' ,args=('actualizado correctamente',)))
    
    except Exception as e:
        return HttpResponse(e)
#Este metodo se encarga de cargarme el formulario para crear un empleado desde un movil 
def crearEmpleadoMovil(request):
    try:
        return render(request,'doctorshots/crear-empleado-movil.html')
    except Exception as e:
        return HttpResponse(e)
#Este metodo Elimina un empleado
def eliminarEmpleado(request,id):
    try:
        q = Usuarios.objects.get(pk=id)
        q.delete()
        return  HttpResponseRedirect(reverse('doctorshots:formempleado',args=('Eliminado',)))
    except Exception as e:
        return HttpResponse(e)

'''PRODUCTOS INVENTARIO'''
#Metodo que despliega el formulario Productos en la pantalla
def formularioProductos(request,mensaje):
    try:
        ses = request.session.get('logueado',False)
        if ses and ses[3]=='2':
            #CApturamos todas las categorias 
            c = CategoriaProducto.objects.all()
            print(c)
            #Capturamos todos los prpdutos
            p = Productos.objects.all()
            
            contexto= {'productos': p, 'categorias':c, 'mensaje': mensaje}
            return render(request,'doctorshots/form-crear-producto.html',contexto)
    except Exception as e:
        return HttpResponse(e)
#MEtodo que me guarda un producto
def guardarProducto(request):
    try:
        c = request.POST['categoria']
        h = request.POST.get('habilitado', 'off') == 'on'

        print(h)                                     
        producto = Productos(
            codigoProducto = request.POST['codigoProducto'],
            nombreProducto= request.POST['nombreProducto'],
            categoria= CategoriaProducto.objects.get(pk=c),
            presentacionProducto = request.POST['presentacionProducto'],
            nacionalidad= request.POST['nacionalidad'],
            precioVenta = request.POST['precioVenta'],
            precioCompra = request.POST['precioCompra'],
            cantidad = request.POST['cantidad'],
            habilitado = h

        )
        producto.save()
        return HttpResponseRedirect(reverse ('doctorshots:formproductos' ,args=('GuardadoCorrectamente',)))
    except Exception as e:
        
        return HttpResponseRedirect(reverse ('doctorshots:formproductos' ,args=(e,)))
#Metodo que me lista los productos    
def verProducto(request,id):
    try:
        p= Productos.objects.get(pk=id)
        diccionario = model_to_dict(p)
        return JsonResponse(diccionario)
    except Exception as e:
        return HttpResponse(e)
#MEtodo que me crea un producto    
def crearProductoMovil(request):
    try:
        return render(request,'doctorshots/crear-producto-movil.html')
    except Exception as e:
        return HttpResponse(e)
#MEtodo que me carga el formulario editar producto
def formularioEditarProducto(request,id):
    try:
        ses = request.session.get('logueado',False)
        if ses and ses[3]=='2':           
            p = Productos.objects.get(pk=id)
            print(p.categoria)
            c = CategoriaProducto.objects.get(descripcion=p.categoria)
            print(c)
            return render(request,'doctorshots/form-editar-producto.html',{'producto':p, 'categoria': c})
        else:
            return render(request,'doctorshots/index.html',{'s':'fallo'})
            
    except Exception as e:        
        return HttpResponse(e)
#Metodo que toma los datos del formulario editar y los actualiza
def actualizarProducto(request):
    try:
        h= request.POST['habilitado']
        if h == 'on':
            h= True
        else:
            h= False
            
        id = request.POST['id']
        p = Productos.objects.get(pk=id)
        p.codigoProducto= request.POST['codigoProducto']
        p.nombreProducto = request.POST['nombreProducto']
        p.precioCompra = request.POST['precioCompra']
        p.precioVenta= request.POST['precioVenta']
        p.cantidad = request.POST['cantidad']
        p.habilitado = h
        p.save()
        return HttpResponseRedirect(reverse('doctorshots:formproductos',args=('Actualizado correctamente',)))
    except Exception as e:
        return HttpResponse(e)
#MEtodo que elimina el producto
def eliminarProducto(request,id):
    try:
        p = Productos.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect(reverse('doctorshots:formproductos',args=('ELiminado con exito',)))
    except Exception as e:
        return HttpResponseRedirect(e)