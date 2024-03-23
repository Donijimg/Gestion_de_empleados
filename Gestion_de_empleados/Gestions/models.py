from django.db import models

class Salario(models.Model):
    valor_cobrar_año = models.DecimalField(max_digits=10, decimal_places=2)
    pago_extra_diciembre = models.DecimalField(max_digits=10, decimal_places=2)

class Puesto(models.Model):
    puesto_trabajo = models.CharField(max_length=100)
    nombre_cargo = models.CharField(max_length=100)
    descripcion_cargo = models.CharField(max_length=100)
    salario_cargo = models.IntegerField()
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE)

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

class Poblacion(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    direccion_codigo_postal = models.CharField(max_length=100)
    poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)




