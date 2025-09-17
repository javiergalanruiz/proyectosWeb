from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "persona_app"

urlpatterns = [
    path('',views.InicioView.as_view(), name='inicio'),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-by-area/<shortname>', views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('listar-empleados-admin/', views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/<id>', views.ListaHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(),name='ver-empleado'),  #El <pk> es como el id, se usa para obtener el id unico para identificar el registro
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name= 'guardado'),
    path('eliminado/', views.vistaEliminada.as_view(), name= 'eliminado'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name= 'modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name= 'eliminar_empleado'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)