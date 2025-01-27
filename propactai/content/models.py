from django.db import models

# Modelo para Clausula
class Clausula(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=2000)

    def __str__(self):
        return self.titulo
    class Meta:
        db_table = 'content_clausula'


# Modelo para Contrato
class Contrato(models.Model):
    titulo = models.CharField(max_length=255)
    numero_contrato = models.CharField(max_length=100, unique=True)
    nombre_proveedor = models.CharField(max_length=255)
    nombre_cliente = models.CharField(max_length=255)
    objeto = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    terminos = models.TextField()

    def __str__(self):
        return self.titulo
    class Meta:
        db_table = 'content_contrato'
