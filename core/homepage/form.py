from django.forms import *

from core.apps.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['dui','nombre','apellido']
        labels = {'dui':'DUI'}
        widgets = {
            'dui': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su numero de dui',
                    'autocomplete':'off'
                }
            )
        }