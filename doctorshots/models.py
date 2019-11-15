from django.db import models

# Create your models here.
class Usuarios(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombres= models.CharField(max_length=50, default='')
    usuario = models.CharField(max_length=45, unique=True)
    clave = models.CharField(max_length=50)
    ROLES=(
        ('1','empleado'),
        ('2','administrador'),
        ('3','usuario')
    )
    Rol= models.CharField(max_length=1, choices=ROLES, default='1')
    
    #METODOS
    def __str__(self):
        return self.usuario

class CategoriaProducto(models.Model):
    descripcion= models.CharField(max_length=45,default='')
    def __str__(self):
        return self.descripcion
            
class Productos(models.Model):
    codigoProducto = models.CharField(max_length=15,  unique=True)
    nombreProducto = models.CharField(max_length=45 )
    categoria = models.ForeignKey(CategoriaProducto, on_delete= models.DO_NOTHING)
    tipos= (
        ('1','330 ml'),
        ('2','375 ml'),
        ('3','750 ml'),
        ('4','1000 ml'),
        ('5','2000 ml')                
    )
    presentacionProducto = models.CharField(max_length=1,choices=tipos,default='')
    nacionalidad = models.CharField(max_length=45)
    habilitado = models.BooleanField(default=True)
    precioVenta = models.FloatField()
    precioCompra = models.FloatField()
    cantidad = models.IntegerField()
    habilitado = models.BooleanField(default=True)
    #Metodos 
    def __str__(self):
        return self.nombreProducto

class Mesas(models.Model):
    numeroMesa= models.CharField(max_length=2)
    disponible= models.BooleanField(default=True)

class Ventas(models.Model):
    mesero = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Mesas, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    estado = models.BooleanField(default=True)
    fecha = models.CharField(max_length=40, default='0000-00-00 00:00:00.000000')

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.DO_NOTHING)
    producto =models.ForeignKey(Productos, on_delete=models.DO_NOTHING)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    

