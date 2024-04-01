from django.db import models

class Salario(models.Model):
    valor_bruto_año = models.IntegerField(null=False, blank=False)
    extra_junio = models.BooleanField(default=False)
    extra_diciembre = models.BooleanField(default=False)

    def __str__(self):
        return self.valor_bruto_año

class Puesto(models.Model):
    nombre_puesto = models.CharField(max_length=15, blank=False, null=False)
    descripcion = models.TextField(null=False)
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE, related_name='puestos')
  
    def __str__(self):
        return self.nombre_puesto

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=15, blank=False, null=False)
    codigo_pais = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.nombre_pais

class Poblacion(models.Model):
    nombre_poblacion = models.CharField(max_length=15, blank=False, null=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='poblaciones')

    def __str__(self):
        return self.nombre_poblacion

class Fabrica(models.Model):
    nombre_fabrica = models.CharField(max_length=15, blank=False, null=False)
    direccion_fabrica = models.CharField(max_length=50, blank=False, null=False)
    codigo_postal = models.CharField(max_length=5, blank=False, null=False)
    poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE, related_name='fabricas')

    def __str__(self):
        return self.nombre_fabrica
    
class Empleado(models.Model):
    documento = models.CharField(max_length=10, blank=False, null=False)
    nombre_empleado = models.CharField(max_length=15, blank=False, null=False)
    nombre_apellido = models.CharField(max_length=15, blank=False, null=False)
    correo_electronico = models.EmailField(max_length=75, blank=False, null=False)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, related_name='empleados')
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, related_name='empleados')

    def __str__(self):
        return self.documento

