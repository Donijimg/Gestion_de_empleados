from django.db import models

class Salario(models.Model):
    amount = models.CharField(max_length=10, null=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

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




