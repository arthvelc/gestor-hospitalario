
from django import forms
from .models import Servicio, Paciente, Pago

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre_servicio', 'costo_servicio']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_paciente', 'apellido_paciente', 'edad_paciente']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['id_servicio', 'id_paciente', 'fecha_pago', 'monto', 'metodo_pago']
