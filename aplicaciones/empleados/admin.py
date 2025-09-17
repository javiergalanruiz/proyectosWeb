from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)


#Decoradores para trabajar en el administrador de Django a la hora de insertar empleados
class EmpleadoAdmin(admin.ModelAdmin):  #Listan los campos que quiera en el administrador de djanto
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
    )
    #
    def full_name(self, obj):   #Funcion para agregar el campo full_name, que no es un campo de la tabla
        #toda la operacion
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('departamento','job','habilidades')

    filter_horizontal = ('habilidades',)
admin.site.register(Empleado, EmpleadoAdmin)