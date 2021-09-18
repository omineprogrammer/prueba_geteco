from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateTimeInput
from django.utils import timezone

from .models import *
from ..widgets import *
from tempus_dominus.widgets import DatePicker, DateTimePicker

        
class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre',]
        widgets = {'nombre': CustomTextInput(),}        
    
        
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre',]
        widgets = {'nombre': CustomTextInput(),}        
    
        
class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = [
            'tiempo_atencion',
            'tiempo_fin_atencion',
            'empresa',
            'ciudad',
            'asunto',
            'respuesta',
            'fecha_solicitud',
        ]
        widgets = {
            'fecha_solicitud': DatePicker(
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True}
            ),
            'tiempo_atencion': DateTimePicker(
                options={
                    'useCurrent': True,
                    'format': 'DD/MM/YYYY hh:mm',
                    'collapse': True
                },
                attrs={
                    'icon_toggle': True,
                    'autocomplete': "disabled",
                    'append': 'fa fa-calendar',

                },
            ),
            'tiempo_fin_atencion': DateTimePicker(
                options={
                    'useCurrent': True,
                    'format': 'DD/MM/YYYY hh:mm',
                    'collapse': True
                },
                attrs={
                    'icon_toggle': True,
                    'autocomplete': "disabled",
                    'append': 'fa fa-calendar',

                },
            ),
            'empresa': CustomSelect(),
            'ciudad': CustomSelect(),
            'asunto': CustomTextInput(),
            'respuesta': CustomTextarea(),
        }

    def clean_fecha_solicitud(self):
        data = self.cleaned_data['fecha_solicitud']
        print(f'clean_fecha_solicitud: {type(data)} {data}')
        if data > datetime.today().date():
            raise ValidationError(f"La fecha superior a la actual.")
        return data

    def clean_tiempo_atencion(self):
        data = self.cleaned_data['tiempo_atencion']
        print(f'clean_tiempo_atencion: {type(data)} {data}')
        if data > timezone.now():
            raise ValidationError(f"La fecha superior a la actual.")
        return data

    def clean_tiempo_fin_atencion(self):
        data = self.cleaned_data['tiempo_fin_atencion']
        print(f'clean_tiempo_fin_atencion: {type(data)} {data}')
        if data > timezone.now():
            raise ValidationError(f"La fecha superior a la actual.")
        return data

