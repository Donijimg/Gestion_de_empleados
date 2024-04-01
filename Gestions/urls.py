from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    
    path('registrar_pais/', views.registrar_pais, name="registrar_pais"),
    path('save_pais/', views.save_pais, name="save_pais"),
    path('registrar_poblacion/', views.registrar_poblacion, name="registrar_poblacion"),
    path('registrar_fabrica/', views.registrar_fabrica, name="registrar_fabrica"),
    path('registrar_salario/', views.registrar_salario, name="registrar_salario"),
    path('registrar_puesto/', views.registrar_puesto, name="registrar_puesto"),
    path('registrar_empleado/', views.registrar_empleado, name="registrar_empleado"),
    path('listar_empleados/', views.listar_empleados, name="listar_empleados"),
    path('listar_salarios/', views.listar_salarios, name="listar_salarios"),
    path('listar_fabricas/', views.listar_fabricas, name="listar_fabricas"),
    path('listar_puestos/', views.listar_puestos, name="listar_puestos"),
    path('listar_paises/', views.listar_paises, name="listar_paises"),
    path('listar_poblaciones/', views.listar_poblaciones, name="listar_poblaciones"),
    path('tabla_empleado/', views.tabla_empleado, name="tabla_empleado"),
    path('editar_pais/<int:pais_id>/', views.editar_pais, name="editar_pais"),
    path('editar_poblacion/<int:poblacion_id>/', views.editar_poblacion, name="editar_poblacion"),
    path('editar_fabrica/<int:fabrica_id>/', views.editar_fabrica, name="editar_fabrica"),
    path('editar_salario/<int:salario_id>/', views.editar_salario, name="editar_salario"),
    path('editar_puesto/<int:puesto_id>/', views.editar_puesto, name="editar_puesto"),
    path('editar_empleado/<int:empleado_id>/', views.editar_empleado, name="editar_empleado"),
    path('recuperar_pais/', views.recuperar_pais, name="recuperar_pais"),
    path('recuperar_poblacion/', views.recuperar_poblacion, name="recuperar_poblacion"),
    path('recuperar_fabrica/', views.recuperar_fabrica, name="recuperar_fabrica"),
    path('recuperar_salario/', views.recuperar_salario, name="recuperar_salario"),
    path('recuperar_puesto/', views.recuperar_puesto, name="recuperar_puesto"),
    path('recuperar_empleado/', views.recuperar_empleado, name="recuperar_empleado"),
    path('eliminar_poblacion/', views.eliminar_poblacion, name="eliminar_poblacion"),
    path('eliminar_fabrica/', views.eliminar_fabrica, name="eliminar_fabrica"),
    path('eliminar_salario/', views.eliminar_salario, name="eliminar_salario"),
    path('eliminar_puesto/', views.eliminar_puesto, name="eliminar_puesto"),
    path('eliminar_empleado/', views.eliminar_empleado, name="eliminar_empleado"),
    path('eliminar_pais/', views.eliminar_pais, name="eliminar_pais"),
    path('save_poblacion/', views.save_poblacion, name="save_poblacion"),
    path('save_fabrica/', views.save_fabrica, name="save_fabrica"),
    path('save_salario/', views.save_salario, name="save_salario"),
    path('save_puesto/', views.save_puesto, name="save_puesto"),
    path('save_empleado/', views.save_empleado, name="save_empleado"),
]



