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
    categorias=(
        ('1','Cervezas'),
        ('2','Wisckeys'),
        ('3','Rones'),
        ('4','Tequilas'),
        ('5','Vodcas'),
        ('6','vinos'),
        ('7','Shots') ,
        ('8','Aguardientes'),
        ('9','Gaseosas')
    )    
    tipo = models.CharField(max_length=1,choices=categorias)
    descripcion= models.CharField(max_length=45,default='')
    def __str__(self):
        return self.descripcion
            
class Productos(models.Model):
    codigoProducto = models.CharField(max_length=15,  unique=True)
    nombreProducto = models.CharField(max_length=45 )
    categoria = models.ForeignKey(CategoriaProducto, on_delete= models.DO_NOTHING)
    tipos= (
        ('1','330 ml'),
        ('2','375ml'),
        ('3','750 ml'),
        ('4','1000ml'),
        ('5','2000')                
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


