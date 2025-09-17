from django import forms

from .models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad',)
        widgets = {     #Personalización del formulario
            'titulo': forms.TextInput(
                attrs = {
                    'paceholder': 'Ingrese texto aquí',
                }
            )
        }
    
    #Función para validar que el numero introducido sea mayor que 10
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad