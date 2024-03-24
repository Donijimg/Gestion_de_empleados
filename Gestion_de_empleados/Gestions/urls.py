from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name="inicio"),
    path('salario/', views.salario, name="salarios"),
    path('guardado/', views.guardado, name = "guardado"),
    path('puesto/',views.puesto, name= "puesto"),
    path('guardarpuesto/',views.guardarpuesto, name= "guardarpuesto"),
    path('listarpuestos/<str:nombre_cargo>', views.listarpuestos, name="listarpuestos")



]