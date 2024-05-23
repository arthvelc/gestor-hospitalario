from django.contrib import admin

# Register your models here.
# myapp/admin.py

from .models import (
    Servicio, Paciente, Pago, HistorialMedico, Especialidad,
    Doctor, Cita, Recepcionista, Consultorio, HorarioConsultorio,
    Receta, Medicamento, Inventario, Bitacora, Usuario
)

admin.site.register(Servicio)
admin.site.register(Paciente)
admin.site.register(Pago)
admin.site.register(HistorialMedico)
admin.site.register(Especialidad)
admin.site.register(Doctor)
admin.site.register(Cita)
admin.site.register(Recepcionista)
admin.site.register(Consultorio)
admin.site.register(HorarioConsultorio)
admin.site.register(Receta)
admin.site.register(Medicamento)
admin.site.register(Inventario)
admin.site.register(Bitacora)
admin.site.register(Usuario)

