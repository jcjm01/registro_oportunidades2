from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    en_stock = models.BooleanField(default=True)  # Asegúrate de que este campo esté defini
    
    def __str__(self):
        return self.nombre

class Oportunidad(models.Model):
    nombre = models.CharField(max_length=100,default='Nombre por defecto')
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_cierre_estimada = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre
