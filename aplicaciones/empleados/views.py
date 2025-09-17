from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( 
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
    
#model
from .models import Empleado
#forms
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    """Vista que carga la pagina de incio"""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 3
    ordering = 'id'
    context_object_name = 'empleados'
    #model = Empleado       Si tenemos un get_queryset, no hace falta obtener el model

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        print(palabra_clave)
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'id'
    context_object_name = 'empleados'
    model = Empleado       #Si tenemos un get_queryset, no hace falta obtener el model

    

class ListByAreaEmpleado(ListView):
    #Lista Empleados de un Área
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self): #Filtro usando la barra de navegación como parametro
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(departamento__short_name = area)
        return lista
    """
    queryset = Empleado.objects.filter(     #Se cambia model por queryset cuando se trata de aplicar filtros
        departamento__name= 'Contabilidad'
    )"""


class ListEmpleadosByKword(ListView):
    model = Empleado
    template_name = "persona/by_kword.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        print('*********')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista
    

class ListaHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_h = self.kwargs['id']
        empleado = Empleado.objects.get(id=id_h)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs): #redefine el contexto de la clase
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
class SuccessView(TemplateView):
    template_name = "persona/success.html"

class vistaEliminada(TemplateView):
    template_name = "persona/eliminado.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm  #Persolanizacion del formulario en el template add.html
    template_name = "persona/add.html"
    #fields = ('__all__') # Con esto se cargan todos los campos del modelo en el formulario web
    #fields = ['first_name', 'last_name','job','departamento','habilidades','avatar']
    success_url = reverse_lazy('persona_app:empleados_admin') #es mas conveniente hacerlo de esta forma
    #'/success'Recarga la pagina de success # '.' Recarga la misma página

    #Interceptamos el metodo de form_valid() asegura que django ha validado los datos 
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save() #Guarda el formulario en la base de datos y asigna los datos en la variable empleado
        empleado.full_name = empleado.first_name +' '+ empleado.last_name
        empleado.save() #guardamos de nuevo empleado que es instancia de form, para que full_name se guarde.
        print(empleado)
        return super(EmpleadoCreateView, self).form_valid(form) #


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['first_name', 'last_name','job','departamento','habilidades']
    template_name = "persona/update.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs): #Se utiliza para guardar datos antes de haber sido validados por el form_valid
        self.object = self.get_object()
        print('*********Metodo Post*************')
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form): #Se utiliza para guardar datos despues de haber sido validados por el formulario
        print('*********Metodo Valid*************')
        return super(EmpleadoUpdateView, self).form_valid(form) #
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
    """
    def delete(self, request, *args, **kwargs):
        
        Call the delete() method on the fetched object and then redirect to the
            success URL.
        
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
    """