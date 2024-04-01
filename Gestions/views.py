from django.shortcuts import render
from django.http import HttpResponse
from .models import Salario, Empleado, Fabrica, Pais, Poblacion, Puesto



def index(request):
    return render(request, 'index.html', {})

def registrar_pais(request):
    return render(request, 'registrar_pais.html', {})

def save_pais(request):
    nombre_pais = request.POST['nombre_pais']
    new_pais = Pais.objects.create(nombre_pais=nombre_pais)
    return HttpResponse(f"Se registró el país {new_pais.nombre_pais}.")

# def registrar_poblacion(request):
#     paises = Pais.objects.all()
#     return render(request, 'registrar_poblacion.html', {
#         'paises': paises
#     })

# def save_poblacion(request):
#     nombre_poblacion = request.POST['nombre_poblacion']
#     pais_id = request.POST['pais_id']
#     pais = Pais.objects.get(id=pais_id)
#     new_poblacion = Poblacion.objects.create(nombre_poblacion=nombre_poblacion, pais=pais)
#     return HttpResponse(f"Se registró la población {new_poblacion.nombre_poblacion} localizada en {pais.nombre_pais}")

# def registrar_fabrica(request):
#     poblaciones = Poblacion.objects.all()
#     return render(request, 'registrar_fabrica.html', {
#         'poblaciones': poblaciones
#     })

# def save_fabrica(request):
#     nombre_fabrica = request.POST['nombre_fabrica']
#     direccion_fabrica = request.POST['direccion_fabrica']
#     codigo_postal = request.POST['codigo_postal']
#     poblacion_id = request.POST['poblacion_id']
#     poblacion = Poblacion.objects.get(id=poblacion_id)
#     new_fabrica = Fabrica.objects.create(nombre_fabrica=nombre_fabrica, direccion_fabrica=direccion_fabrica, codigo_postal=codigo_postal, poblacion = poblacion)
#     return HttpResponse(f"Se registró la fabrica {new_fabrica.nombre_fabrica} localizada en la población {poblacion.nombre_poblacion}")

# def registrar_salario(request):
#     return render(request, 'registrar_salario.html', {})

# def save_salario(request):
#     valor_bruto_año = request.POST['valor_bruto_año']
#     if 'extra_junio' in request.POST:
#         extra_junio = True
#     else:
#         extra_junio = False
#     if 'extra_diciembre' in request.POST:
#         extra_diciembre = True
#     else:
#         extra_diciembre = False
#     new_salario = Salario.objects.create(valor_bruto_año=valor_bruto_año, extra_junio=extra_junio, extra_diciembre=extra_diciembre)
#     return HttpResponse(f"Se registró el salario")


# def registrar_puesto(request):
#     salarios = Salario.objects.all()
#     return render(request, 'registrar_puesto.html', {
#         'salarios': salarios
#     })

# def save_puesto(request):
#     nombre_puesto = request.POST['nombre_puesto']
#     descripcion = request.POST['descripcion']
#     salario_id = request.POST['salario_id']
#     salario = Salario.objects.get(id=salario_id)
#     new_puesto = Puesto.objects.create(nombre_puesto=nombre_puesto, descripcion=descripcion, salario=salario)
#     return HttpResponse(f"Se registró el puesto {new_puesto.nombre_puesto}.")



# def tabla_empleado(request):
#     return render(request, 'tabla_empleado.html', {})

# def registrar_empleado(request):
#     fabricas = Fabrica.objects.all()
#     puestos = Puesto.objects.all()
#     return render(request, 'registrar_empleado.html', {
#         'fabricas': fabricas,
#         'puestos': puestos
#     })

# def save_empleado(request):
#     nombre_empleado = request.POST['nombre_empleado']
#     documento = request.POST['documento']
#     email = request.POST['email']
#     direccion_empleado = request.POST['direccion_empleado']
#     fabrica_id = request.POST['fabrica_id']
#     fabrica = Fabrica.objects.get(id=fabrica_id)
#     puesto_id = request.POST['puesto_id']
#     puesto = Puesto.objects.get(id=puesto_id)
#     new_empleado = Empleado.objects.create(nombre_empleado=nombre_empleado, documento=documento, email=email ,direccion_empleado=direccion_empleado, fabrica=fabrica, puesto=puesto)
#     return HttpResponse(f"Se registró el empleado {new_empleado.nombre_empleado} con el puesto de {puesto.nombre_puesto} en la fabrica {fabrica.nombre_fabrica}")


# def listar_empleados(request):
    
#     filtro_documento = request.GET.get('documento')    
#     filtro_nombre = request.GET.get('nombre_empleado')
#     filtro_apellido =request.GET.get('nombre_apellido')
#     filtro_correo=request.GET.get('correo_electronico')
#     filtro_puesto=request.GET.get('nombre_puesto')
#     filtro_fabrica=request.GET.get('nombre_fabrica')
    

#     empleados = Empleado.objects.all()
#     puestos = Puesto.objects.all()
#     fabricas = Fabrica.objects.all()
  

#     if filtro_documento:
#         empleados = empleados.filter(documento__icontains=filtro_documento)
#     if filtro_nombre:
#         empleados = empleados.filter(nombre_empleado__icontains=filtro_nombre)
#     if filtro_apellido:
#         empleados = empleados.filter(nombre_apellido__icontains=filtro_apellido)
#     if filtro_correo:
#         empleados = empleados.filter(correo_electronico__icontains=filtro_correo)
#     if filtro_puesto:
#         puestos = puestos.filter(nombre_puesto__icontains=filtro_puesto)
#     if filtro_fabrica:
#         fabricas = fabricas.filter(nombre_fabrica__icontains= filtro_fabrica)


#     return render(request, 'lista_empleados.html', {'empleados': empleados, 'puestos': puestos, 'fabricas':fabricas })



# def listar_salarios(request):
#     filtro_puesto = request.GET.get('nombre_puesto')
#     filtro_valor_año = request.GET.get('valor_bruto_año')
#     filtro_junio = request.GET.get('extra_junio')
#     filtro_diciembre = request.GET.get('extra_diciembre')


#     puestos = Puesto.objects.all()
#     salarios = Salario.objects.all()

#     if filtro_puesto:
#         puestos = puestos.filter(nombre_puesto__icontains=filtro_puesto)
#     if filtro_valor_año:
#         salarios = salarios.filter(valor_bruto_año__icontains=filtro_valor_año)                  
#     if filtro_junio:
#         salarios = salarios.filter(extra_junio__icontains=filtro_junio)                  
#     if filtro_diciembre:
#         salarios = salarios.filter(extra_diciembre__icontains=filtro_diciembre)                  

#     return render(request, 'lista_salarios.html', {'salarios': salarios, 'puestos': puestos, 'salarios': salarios  })


# def listar_fabricas(request):
#     filtro_fabrica = request.GET.get('nombre_fabrica')
#     filtro_direccion = request.GET.get ('direccion_fabrica')
#     filtro_cdpostal = request.GET.get ('codigo_postal')

#     fabricas = Fabrica.objects.all()
    
#     if filtro_fabrica:
#         fabricas = fabricas.filter(nombre_fabrica__icontains=filtro_fabrica)                  
#     if filtro_direccion:
#         fabricas = fabricas.filter(direccion_fabrica__icontains=filtro_direccion)                  
#     if filtro_cdpostal:
#         fabricas = fabricas.filter(direccion_fabrica__icontains=filtro_cdpostal)   

#     return render(request, 'listar_fabricas.html', {'fabricas': fabricas})


# def listar_puestos(request):

#     filtro_puesto= request.GET.get('nombre_puesto')
#     filtro_descripcion= request.GET.get('descripcion')
#     filtro_documento = request.GET.get('documento')    
#     filtro_nombre = request.GET.get('nombre_empleado')
#     filtro_apellido = request.GET.get('nombre_apellido')

#     puestos = Puesto.objects.all()
#     empleados = Empleado.objects.all()
    

#     if filtro_puesto:
#         puestos = puestos.filter(nombre_puesto__icontains=filtro_puesto)
#     if filtro_descripcion:
#         puestos = puestos.filter(descripcion__icontains=filtro_descripcion)
#     if filtro_documento:
#         empleados = empleados.filter(documento__icontains=filtro_documento)
#     if filtro_nombre:
#         empleados = empleados.filter(nombre_empleado__icontains=filtro_nombre)
#     if filtro_apellido:
#         empleados = empleados.filter(nombre_apellido__icontains=filtro_apellido)


#     return render(request, 'listar_puestos.html', {'puestos': puestos, 'empleados': empleados})

# def listar_paises(request):
#     filtro_pais= request.GET.get('nombre_pais')
#     filtro_codigo= request.GET.get('codigo_pais')
#     filtro_poblacion=request.GET.get('nombre_poblacion')

#     paises = Pais.objects.all()
#     poblaciones = Poblacion.objects.all()

#     if filtro_pais:
#         paises = paises.filter(nombre_pais__icontains=filtro_pais)
#     if filtro_codigo:
#         paises = paises.filter(codigo_pais__icontains=filtro_codigo)
#     if filtro_poblacion:
#         poblaciones = poblaciones.filter(nombre_poblacion__icontains=filtro_poblacion)

#     return render(request, 'listar_paises.html', {'paises': paises, 'poblaciones': poblaciones })

# def listar_poblaciones(request):
#     filtro_pais= request.GET.get('nombre_pais')
#     filtro_poblacion=request.GET.get('nombre_poblacion')

#     poblaciones = Poblacion.objects.all()
#     paises = Pais.objects.all()
    

#     if filtro_pais:
#         paises = paises.filter(nombre_pais__icontains=filtro_pais)
#     if filtro_poblacion:
#         poblaciones = poblaciones.filter(nombre_poblacion__icontains=filtro_poblacion)

#     return render(request, 'listar_poblaciones.html', {
#         'poblaciones': poblaciones
#     })

# def tabla_empleado(request):
#     return render(request, 'tabla_empleado.html', {})

# def editar_pais(request, pais_id):
#     pais = Pais.objects.get(id=pais_id)
#     if request.method == 'POST':
#         nombre_pais = request.POST['nombre_pais']
#         pais.nombre_pais = nombre_pais
#         save_pais(pais)
#         return HttpResponse(f"Se actualizó el país {pais.nombre_pais}.")
#     return render(request, 'editar_pais.html', {'pais': pais})

# def editar_poblacion(request, poblacion_id):
#     poblacion = Poblacion.objects.get(id=poblacion_id)
#     if request.method == 'POST':
#         nombre_poblacion = request.POST['nombre_poblacion']
#         poblacion.nombre_poblacion = nombre_poblacion
#         save_poblacion(poblacion)
#         return HttpResponse(f"Se actualizó la población {poblacion.nombre_poblacion}.")
#     return render(request, 'editar_poblacion.html', {'poblacion': poblacion})

# def editar_fabrica(request, fabrica_id):
#     fabrica = Fabrica.objects.get(id=fabrica_id)

#     if request.method == 'POST':
#         nombre_fabrica = request.POST['nombre_fabrica']
#         direccion_fabrica = request.POST['direccion_fabrica']
#         codigo_postal = request.POST['codigo_postal']
#         poblacion_id = request.POST['poblacion_id']
#         poblacion = Poblacion.objects.get(id=poblacion_id)
#         fabrica.nombre_fabrica = nombre_fabrica
#         fabrica.direccion_fabrica = direccion_fabrica
#         fabrica.codigo_postal = codigo_postal
#         fabrica.poblacion = poblacion
#         save_fabrica(fabrica)
#         return HttpResponse(f"Se actualizó la fábrica {fabrica.nombre_fabrica}.")
#     poblaciones = Poblacion.objects.all()
#     return render(request, 'editar_fabrica.html', {'fabrica': fabrica, 'poblaciones': poblaciones})

# def editar_salario(request, salario_id):
#     salario = Salario.objects.get(id=salario_id)
#     if request.method == 'POST':
#         valor_bruto_año = request.POST['valor_bruto_año']
#         extra_junio = 'extra_junio' in request.POST
#         extra_diciembre = 'extra_diciembre' in request.POST
#         salario.valor_bruto_año = valor_bruto_año
#         salario.extra_junio = extra_junio
#         salario.extra_diciembre = extra_diciembre
#         save_salario(salario)
#         return HttpResponse(f"Se actualizó el salario.")
#     return render(request, 'editar_salario.html', {'salario': salario})

# def editar_puesto(request, puesto_id):
#     puesto = Puesto.objects.get(id=puesto_id)
#     if request.method == 'POST':
#         nombre_puesto = request.POST['nombre_puesto']
#         descripcion = request.POST['descripcion']
#         salario_id = request.POST['salario_id']
#         salario = Salario.objects.get(id=salario_id)
#         puesto.nombre_puesto = nombre_puesto
#         puesto.descripcion = descripcion
#         puesto.salario = salario
#         save_puesto(puesto)
#         return HttpResponse(f"Se actualizó el puesto {puesto.nombre_puesto}.")
#     salarios = Salario.objects.all()
#     return render(request, 'editar_puesto.html', {'puesto': puesto, 'salarios': salarios})

# def editar_empleado(request, empleado_id):
#     empleado = Empleado.objects.get(id=empleado_id)
#     if request.method == 'POST':
#         nombre_empleado = request.POST['nombre_empleado']
#         documento = request.POST['documento']
#         correo_electronico = request.POST['correo_electronico']
#         direccion_empleado = request.POST['direccion_empleado']
#         fabrica_id = request.POST['fabrica_id']
#         fabrica = Fabrica.objects.get(id=fabrica_id)
#         puesto_id = request.POST['puesto_id']
#         puesto = Puesto.objects.get(id=puesto_id)
#         empleado.nombre_empleado = nombre_empleado
#         empleado.documento = documento
#         empleado.correo_electronico = correo_electronico
#         empleado.direccion_empleado = direccion_empleado
#         empleado.fabrica = fabrica
#         empleado.puesto = puesto
#         save_empleado(empleado)
#         return HttpResponse(f"Se actualizó el empleado {empleado.nombre_empleado}.")
#     return render(request, 'editar_empleado.html', {'empleado': empleado })

# def recuperar_pais(request):
#     pais_id = request.GET['id']
#     pais = Pais.objects.get(id=pais_id)
#     save_pais(pais)
#     return render(request, 'recuperar_pais.html', {'pais': pais})

# def recuperar_poblacion(request):
#     poblacion_id = request.GET['id']
#     poblacion = Poblacion.objects.get(id=poblacion_id)
#     save_poblacion(poblacion)
#     return render(request, 'recuperar_poblacion.html', {'poblacion': poblacion})

# def recuperar_fabrica(request):
#     fabrica_id = request.GET['id']
#     fabrica = Fabrica.objects.get(id=fabrica_id)
#     save_fabrica(fabrica)
#     return render(request, 'recuperar_fabrica.html', {'fabrica': fabrica})

# def recuperar_salario(request):
#     salario_id = request.GET['id']
#     salario = Salario.objects.get(id=salario_id)
#     save_salario(salario)
#     return render(request, 'recuperar_salario.html', {'salario': salario})

# def recuperar_puesto(request):
#     puesto_id = request.GET['id']
#     puesto = Puesto.objects.get(id=puesto_id)
#     save_puesto(puesto)
#     return render(request, 'recuperar_puesto.html', {'puesto': puesto})

# def recuperar_empleado(request):
#     empleado_id = request.GET['id']
#     empleado = Empleado.objects.get(id=empleado_id)
#     save_empleado(empleado)
#     return render(request, 'recuperar_empleado.html', {'empleado': empleado})

# def eliminar_poblacion(request):
#     poblacion_id = request.GET['id']
#     poblacion=Poblacion.objects.get(id=poblacion_id).delete()
#     save_poblacion(poblacion)
#     return render(request, 'eliminar_poblacion.html', {'poblacion': poblacion})

# def eliminar_fabrica(request):
#     fabrica_id = request.GET['id']
#     fabrica=Fabrica.objects.get(id=fabrica_id).delete()
#     save_fabrica(fabrica)
#     return render(request, 'eliminar_fabrica.html', {'fabrica': fabrica})

# def eliminar_salario(request):
#     salario_id = request.GET['id']
#     salario=Salario.objects.get(id=salario_id).delete()
#     save_salario(salario)
#     return render(request, 'eliminar_salario.html',{'salario': salario})

# def eliminar_puesto(request):
#     puesto_id = request.GET['id']
#     puesto=Puesto.objects.get(id=puesto_id).delete()
#     save_puesto(puesto)
#     return render(request, 'eliminar_puesto.html',{'puesto': puesto})

# def eliminar_empleado(request):
#     empleado_id = request.GET['id']
#     empleado=Empleado.objects.get(id=empleado_id).delete()
#     save_empleado(empleado)
#     return render(request, 'eliminar_empleado.html',{'empleado': empleado})

# def eliminar_pais(request):
#     pais_id = request.GET['id']
#     pais=Pais.objects.get(id=pais_id).delete()
#     save_pais(pais)
#     return render(request, 'eliminar_pais.html',{'pais': pais})















# views:

# def save_puesto(request):
#     nombre_puesto = request.POST['nombre_puesto']
#     descripcion = request.POST['descripcion']
#     salario_id = request.POST['salario_id']
#     salario = Salario.objects.get(id=salario_id)
#     new_puesto = Puesto.objects.create(nombre_puesto=nombre_puesto, descripcion=descripcion, salario=salario)
#     return HttpResponse(f"Se registró el puesto {new_puesto.nombre_puesto}.")


# listar_puestos.html:
# {% extends "layouts/app.html" %}
# {% block title %}
# <title>Listar Puestos</title>
# {% endblock title %}
# {% block card_title %}
# <h1>Listar Puestos</h1>
# {% endblock card_title %}
# {% block list %}
# {% include "forms/form_listar_puestos.html" %}
# {% endblock list %}

# def listar_puestos(request):
#     filtro_puesto= request.GET.get('nombre_puesto')
#     filtro_descripcion= request.GET.get('descripcion')
#     filtro_documento = request.GET.get('documento')    
#     filtro_nombre = request.GET.get('nombre_empleado')
#     filtro_apellido = request.GET.get('nombre_apellido')
#     puestos = Puesto.objects.all()
#     empleados = Empleado.objects.all()
#     if filtro_puesto:
#         puestos = puestos.filter(nombre_puesto__icontains=filtro_puesto)
#     if filtro_descripcion:
#         puestos = puestos.filter(descripcion__icontains=filtro_descripcion)
#     if filtro_documento:
#         empleados = empleados.filter(documento__icontains=filtro_documento)
#     if filtro_nombre:
#         empleados = empleados.filter(nombre_empleado__icontains=filtro_nombre)
#     if filtro_apellido:
#         empleados = empleados.filter(nombre_apellido__icontains=filtro_apellido)
#     return render(request, 'listar_puestos.html', {'puestos': puestos, 'empleados': empleados})


# form_listar_puestos.html :
# <section class="seccion_formulario">
#   <article class="card">
#     <form action="{% url 'listar_salarios' %}" method="get">
#       <div class="form-group">
#         <label for=""></label>
#         <input type="text" class="form-control" id="" name="" required>
#       </div>
#       <button type="submit">Buscar</button>
#     </form>
#   </article>
# </section>
# <table class="table">
#   <thead>
#     <tr>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     {% for  in %}
#     <tr>
#       <td>{{}}</td>
#     </tr>
#     {% endfor %}
#   </tbody>
# </table>

# models: 
# class Salario(models.Model):
#     valor_bruto_año = models.IntegerField(null=False, blank=False)
#     extra_junio = models.BooleanField(default=False)
#     extra_diciembre = models.BooleanField(default=False)

# class Puesto(models.Model):
#     nombre_puesto = models.CharField(max_length=15, blank=False, null=False)
#     descripcion = models.TextField(null=False)
#     salario = models.ForeignKey(Salario, on_delete=models.CASCADE, related_name='puestos')

# class Pais(models.Model):
#     nombre_pais = models.CharField(max_length=15, blank=False, null=False)
#     codigo_pais = models.CharField(max_length=6, blank=False, null=False)

# class Poblacion(models.Model):
#     nombre_poblacion = models.CharField(max_length=15, blank=False, null=False)
#     pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='poblaciones')

# class Fabrica(models.Model):
#     nombre_fabrica = models.CharField(max_length=15, blank=False, null=False)
#     direccion_fabrica = models.CharField(max_length=50, blank=False, null=False)
#     codigo_postal = models.CharField(max_length=5, blank=False, null=False)
#     poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE, related_name='fabricas')

# class Empleado(models.Model):
#     documento = models.CharField(max_length=10, blank=False, null=False)
#     nombre_empleado = models.CharField(max_length=15, blank=False, null=False)
#     nombre_apellido = models.CharField(max_length=15, blank=False, null=False)
#     correo_electronico = models.EmailField(max_length=75, blank=False, null=False)
#     puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, related_name='empleados')
#     fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, related_name='empleados')

# necesito los archivos htlm corregidos y completados




# <!-- 
# <ul>
#   {% for empleado in empleados %}
#    <a href="#">Editar</a></li>
#   {% endfor %}
# </ul> -->
















# def save_pais(request):
#     nombre_pais = request.POST['nombre_pais']
#     new_pais = Pais.objects.create(nombre_pais=nombre_pais)
#     return HttpResponse(f"Se registró el país {new_pais.nombre_pais}.")



# def save_poblacion(request):
#     nombre_poblacion = request.POST['nombre_poblacion']
#     pais_id = request.POST['pais_id']
#     pais = Pais.objects.get(id=pais_id)
#     new_poblacion = Poblacion.objects.create(nombre_poblacion=nombre_poblacion, pais=pais)
#     return HttpResponse(f"Se registró la población {new_poblacion.nombre_poblacion} localizada en {pais.nombre_pais}")

# def save_fabrica(request):
#     nombre_fabrica = request.POST['nombre_fabrica']
#     direccion_fabrica = request.POST['direccion_fabrica']
#     codigo_postal = request.POST['codigo_postal']
#     poblacion_id = request.POST['poblacion_id']
#     poblacion = Poblacion.objects.get(id=poblacion_id)
#     new_fabrica = Fabrica.objects.create(nombre_fabrica=nombre_fabrica, direccion_fabrica=direccion_fabrica, codigo_postal=codigo_postal, poblacion = poblacion)
#     return HttpResponse(f"Se registró la fabrica {new_fabrica.nombre_fabrica} localizada en la población {poblacion.nombre_poblacion}")

# def save_salario(request):
#     valor_bruto_año = request.POST['valor_bruto_año']
#     if 'extra_junio' in request.POST:
#         extra_junio = True
#     else:
#         extra_junio = False
#     if 'extra_diciembre' in request.POST:
#         extra_diciembre = True
#     else:
#         extra_diciembre = False
#     new_salario = Salario.objects.create(valor_bruto_año=valor_bruto_año, extra_junio=extra_junio, extra_diciembre=extra_diciembre)
#     return HttpResponse(f"Se registró el salario")

# def save_puesto(request):
#     nombre_puesto = request.POST['nombre_puesto']
#     descripcion = request.POST['descripcion']
#     salario_id = request.POST['salario_id']
#     salario = Salario.objects.get(id=salario_id)
#     new_puesto = Puesto.objects.create(nombre_puesto=nombre_puesto, descripcion=descripcion, salario=salario)
#     return HttpResponse(f"Se registró el puesto {new_puesto.nombre_puesto}.")

# def save_empleado(request):
#     nombre_empleado = request.POST['nombre_empleado']
#     documento = request.POST['documento']
#     correo_electronico = request.POST['correo_electronico']
#     direccion_empleado = request.POST['direccion_fabrica']
#     fabrica_id = request.POST['fabrica_id']
#     fabrica = Fabrica.objects.get(id=fabrica_id)
#     puesto_id = request.POST['puesto_id']
#     puesto = Puesto.objects.get(id=puesto_id)
#     new_empleado = Empleado.objects.create(nombre_empleado=nombre_empleado, documento=documento, correo_electronico=correo_electronico ,direccion_empleado=direccion_empleado, fabrica=fabrica, puesto=puesto)
#     return HttpResponse(f"Se registró el empleado {new_empleado.nombre_empleado} con el puesto de {puesto.nombre_puesto} en la fabrica {fabrica.nombre_fabrica}")


# def index(request):
#     return render(request, 'index.html', {})
    
# def registrar_pais(request):
#     paises = Pais.objects.all()
#     return save_pais(request, Pais(), 'registrar_pais.html', {
#         'paises': paises
#     })
# def registrar_poblacion(request):
#     poblaciones = Poblacion.objects.all()
#     return save_poblacion(request, Poblacion(), 'registrar_poblacion.html', {
#         'poblaciones': poblaciones
#     })
# def registrar_fabrica(request):
#     fabricas = Fabrica.objects.all()
#     return save_fabrica(request, Fabrica(), 'registrar_fabrica.html',{
#         'fabricas': fabricas
#     })
# def registrar_salario(request):
#     salarios = Salario.objects.all()
#     return save_salario(request, Salario(), 'registrar_salario.html',{
#         'salarios': salarios
#     })
# def registrar_puesto(request):
#     puestos = Puesto.objects.all()
#     return save_puesto(request, Puesto(), 'registrar_puesto.html',{
#         'puestos': puestos
#     })
# def registrar_empleado(request):
#     empleados = Empleado.objects.all()
#     return save_empleado(request, Empleado(), 'registrar_empleado.html',{
#         'empleados': empleados
#     })
