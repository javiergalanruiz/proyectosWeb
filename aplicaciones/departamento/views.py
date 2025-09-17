from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
# Create your views here.
from .forms import NewDepantamentoForm

from aplicaciones.empleados.models import Empleado
from aplicaciones.departamento.models import Departamento


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'



class NewDepantamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepantamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        depa.save()     #para agregar de esta forma, hay que utilizar este metodo de .save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(    #utilizando este metodo se agrega automaticamente con .create()
            first_name = nombre,
            last_name = apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepantamentoView, self).form_valid(form)