from django.urls import path
from . import views

urlpatterns = [
     path('create/',views.create,name="create"),
    #  path('listado',views.listado,name="listado"),
    # path('storage/<str:name>',views.storage,name="storage"),
    # path('consultar/<int:id>',views.consultar,name="consultar"),
    # path('modificar/<str:name>/<int:id>',views.modificar,name="modificar"),
    # path('eliminar/<int:id>',views.eliminar,name="eliminar"),

]