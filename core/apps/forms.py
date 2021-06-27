from operator import attrgetter

from django.forms import *
from core.apps.models import *
from django import forms

class SubsidioTransporteForm(ModelForm):
    class Meta:
        model = SubsidioTransporte
        fields = ['pertenece','frecuencia_uso','cantidad_buses','cantidad_microbuses']


        widgets = {
            'pertenece': Select(
                attrs={
                    'class': 'form-control form-control-sm col-7',
                }
            ),
            'frecuencia_uso': Select(
                attrs={
                    'class': 'form-control form-control-sm col-3'
                }
            ),
            'cantidad_microbuses': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'cantidad de microbuses utiliza'
                }
            ),
            'cantidad_buses': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'cantidad de buses utiliza'
                }
            ),
        }


    #Hacer validaciones adicionales
    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_buses'] < 0:
            self.add_error('cantidad_buses','La cantidad de buses debe ser una cantidad mayor a 0')
        if cleaned['cantidad_microbuses'] < 0:
            self.add_error('cantidad_microbuses','La cantidad de microbuses debe ser una cantidad mayor a 0')
        return cleaned

class SubsidioTransporteEditForm(ModelForm):
    class Meta:
        model = SubsidioTransporte
        fields = ['pertenece','cantidad_subsidio','frecuencia_uso', 'cantidad_buses', 'cantidad_microbuses']

        widgets = {
            'pertenece': Select(
                attrs={
                    'class': 'form-control form-control-sm col-7',
                }
            ),
            'frecuencia_uso': Select(
                attrs={
                    'class': 'form-control form-control-sm col-3'
                }
            ),
            'cantidad_subsidio': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                }
            ),
            'cantidad_microbuses': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'cantidad de microbuses utiliza'
                }
            ),
            'cantidad_buses': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'cantidad de buses utiliza'
                }
            ),
        }

        # Hacer validaciones adicionales

    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_buses'] < 0:
            self.add_error('cantidad_buses', 'La cantidad de buses debe ser una cantidad mayor a 0')
        if cleaned['cantidad_microbuses'] < 0:
            self.add_error('cantidad_microbuses', 'La cantidad de microbuses debe ser una cantidad mayor a 0')
        return cleaned
class SubsidioAguaForm(ModelForm):
    class Meta:
        model = SubsidioAgua
        fields = ['pertenece', 'cantidad_consumo', 'recibo_agua']
        labels = {'pertenece': 'Beneficiario'}

        widgets = {
            'pertenece': Select(
                attrs={
                    'class': 'form-control form-control-sm',
                }
            ),
            'cantidad_consumo': NumberInput(
                attrs={
                    'class': 'form-control col-md-4',
                    'placeholder': 'cantidad consumida en metros cúbicos'
                }
            ),
            'recibo_agua' : FileInput(
                attrs={
                    'class': 'form-control-file form-control-lg col-5'
                }
            )
        }


    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_consumo'] < 0:
            self.add_error('cantidad_consumo','La cantidad de consumo debe ser una cantidad mayor a 0')
        return cleaned

class SubsidioAguaEditForm(ModelForm):
    class Meta:
        model = SubsidioAgua
        fields = ['pertenece','cantidad_subsidio','cantidad_consumo','verificado','aprobado','recibo_agua']
        labels = {'pertenece': 'Beneficiario'}

        widgets = {
            'pertenece': Select(
                attrs={
                    'class': 'form-control form-control-sm',
                }
            ),
            'cantidad_consumo': NumberInput(
                attrs={
                    'class': 'form-control col-md-4',
                    'placeholder': 'cantidad consumida en metros cúbicos'
                }
            ),
            'cantidad_subsidio': NumberInput(
                attrs={
                    'class': 'form-control col-md-4',
                    'placeholder': 'cantidad consumida en metros cúbicos'
                }
            ),
            'recibo_agua' : FileInput(
                attrs={
                    'class': 'form-control-file form-control-lg col-5'
                }
            )
        }


    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_consumo'] < 0:
            self.add_error('cantidad_consumo','La cantidad de consumo debe ser una cantidad mayor a 0')
        return cleaned

class SubsidioLuzEditForm(ModelForm):
    class Meta:
        model = SubsidioLuz
        fields = ['pertenece','cantidad_subsidio','cantidad_consumo','verificado','aprobado','recibo_luz']
        labels = {'pertenece': 'Beneficiario'}

        widgets = {
            'pertenece': Select(
                attrs={
                    'class': 'form-control form-control-sm'
                }
            ),
            'cantidad_consumo': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'Cantidad consumida en kilowatts por hora (kw/h)'
                }
            ),
            'cantidad_subsidio': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'Cantidad subisidiada por el gobierno'
                }
            ),
            'recibo_luz': FileInput(
                attrs={
                    'class': 'form-control-file form-control-lg col-5',
                    'placeholder': 'Subir imagen de recibo de luz'
                }
            )

        }


    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_consumo'] < 0:
            self.add_error('cantidad_consumo','La cantidad de consumo debe ser una cantidad mayor a 0')
        return cleaned
class SubsidioLuzForm(ModelForm):

    class Meta:
        model = SubsidioLuz
        fields = ['pertenece','cantidad_consumo','recibo_luz']

        widgets = {
            'pertenece':Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'cantidad_consumo':NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                    'placeholder': 'Cantidad consumida en kilowatts por hora (kw/h)'
                }
            ),
            'recibo_luz' : FileInput(
                attrs={
                    'class': 'form-control-file form-control-lg col-5',
                    'placeholder': 'Subir imagen de recibo de luz'
                }
            )

        }

    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_consumo'] < 0:
            self.add_error('cantidad_consumo', 'La cantidad de consumo debe ser una cantidad mayor a 0')
        return cleaned

class SubsidioGasEditForm(ModelForm):
    class Meta:
        model = SubsidioGasLicuado
        fields = ['pertenece','cantidad_consumo','cantidad_subsidio','tipo_establecimiento','num_tarjeta','verificado','aprobado','recibo_luz']
        labels = { 'tipo_establecimiento':'Hogar familiar o negocio de subsitencia'}
        widgets={
             'pertenece': Select(
                 attrs={
                     'class': 'form-control'
                 }
             ),
             'tipo_establecimiento': Select(
                 attrs={
                     'class': 'form-control col-3'
                 }
             ),
             'cantidad_consumo': NumberInput(
                 attrs={
                     'class': 'form-control form-control-sm col-4',
                     'placeholder': 'Cantidad consumida en kilowatts por hora (kw/h)'
                 }
             ),
            'cantidad_subsidio': NumberInput(
                attrs={
                    'class': 'form-control form-control-sm col-4',
                }
            ),
             'num_tarjeta':TextInput(
                 attrs={
                     'class': 'form-control form-control-sm col-4',
                     'placeholder': 'Numero de tarjeta solidaria'
                 }
             ),
             'recibo_luz': FileInput(
                 attrs={
                     'class': 'form-control-file form-control-lg col-5'
                 }
             )
         }

    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_consumo'] < 0:
            self.add_error('cantidad_consumo', 'La cantidad de consumo debe ser una cantidad mayor a 0')
        return cleaned
class SubsidioGasForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['pertenece'].widget.attrs['autofocus'] = True
    class Meta:
        model = SubsidioGasLicuado
        fields = ['pertenece','tipo_establecimiento','cantidad_consumo','num_tarjeta','recibo_luz']
        exclude = ['cantidad_subsidio']
        labels = { 'tipo_establecimiento':'Hogar familiar o negocio de subsitencia'}
        widgets={
             'pertenece': Select(
                 attrs={
                     'class': 'form-control'
                 }
             ),
             'tipo_establecimiento': Select(
                 attrs={
                     'class': 'form-control col-3'
                 }
             ),
             'cantidad_consumo': NumberInput(
                 attrs={
                     'class': 'form-control form-control-sm col-4',
                     'placeholder': 'Cantidad consumida en kilowatts por hora (kw/h)'
                 }
             ),
             'num_tarjeta':TextInput(
                 attrs={
                     'class': 'form-control form-control-sm col-4',
                     'placeholder': 'Numero de tarjeta solidaria'
                 }
             ),
             'recibo_luz': FileInput(
                 attrs={
                     'class': 'form-control-file form-control-lg col-5'
                 }
             )
         }

    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_consumo'] < 0:
            self.add_error('cantidad_consumo', 'La cantidad de consumo debe ser una cantidad mayor a 0')
        return cleaned





