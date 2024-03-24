from django.shortcuts import render
from django.http import HttpResponse
from .models import Salario,Empleado,Fabrica,Pais,Poblacion,Puesto
# Create your views here.
def index(request):
  return render(request, 'index.html', {})

def salario(request):

  return render(request, "salario.html", {})

def guardado(request):
  amount = request.GET['amount']
  salario = Salario(amount = amount)
  salario.save()
  return HttpResponse("Hola")

def puesto(request):
  salario=Salario.objects.all()
  return render (request, 'puesto.html',{
    'salario' : salario
  })

def guardarpuesto(request):
  if request.method != 'POST':
    return HttpResponse("Metodo no soportado")
  nombre= request.POST['nombre']
  descripcion= request.POST['descripcion']
  salario = Salario.objects.get(id=request.POST['salario'])
  puesto= Puesto (nombre=nombre, descripcion=descripcion, salario=salario)
  puesto.save()
  return HttpResponse("puesto de trabajo creado")




def listarpuestos(request,puesto_trabajo):
  cargo = Puesto.objects.get(puesto_trabajo)
  for obj in cargo:
    print(obj.puesto_trabajo)
  return HttpResponse ("lista de places")












def storage(title, id):
  # publication = Publication(title=title)
  # article= Article(id=id)
  # publication.save()
  # article.save()
  return HttpResponse ("guardamos los datos")
  
def consultar(requets,id):
  # publication= Publication.objects.get(id=id)
  # article=Article.objects.all()
  return HttpResponse (f"nombre: {publication.title}, restaurant: {article}")


def modificar(request, title,id):
  # publication=Publication.objects.get(id=id)
  # publication.title=title
  # publication.save()
  return HttpResponse("post actualizado")

def eliminar(request,id):
  # publication=Publication.objects.get(id=id)
  # publication.delete()
  return HttpResponse("post eliminado")


  
  