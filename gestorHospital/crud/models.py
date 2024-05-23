from django.db import models
from django.contrib.auth.hashers import make_password

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=50)
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=50)
    apellido_paciente = models.CharField(max_length=50)
    edad_paciente = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pago(models.Model):
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HistorialMedico(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    enfermedad = models.CharField(max_length=50)
    tipo_sangre = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    altura = models.DecimalField(max_digits=10, decimal_places=2)
    alergias = models.CharField(max_length=50)
    tratamiento = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Doctor(models.Model):
    nombre_doctor = models.CharField(max_length=50)
    apellido_doctor = models.CharField(max_length=50)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    cedula_profesional = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cita(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recepcionista(models.Model):
    nombre_recepcionista = models.CharField(max_length=50)
    apellido_recepcionista = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Consultorio(models.Model):
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    horario_consultorio = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HorarioConsultorio(models.Model):
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_recepcionista = models.ForeignKey(Recepcionista, on_delete=models.CASCADE)
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Receta(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=50)
    tratamiento = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=50)
    costo_medicamento = models.DecimalField(max_digits=10, decimal_places=2)
    caducidad_medicamento = models.DateField()
    disponibilidad_medicamento = models.IntegerField()
    formula_activa = models.CharField(max_length=50)
    presentacion_medicamento = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventario(models.Model):
    id_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bitacora(models.Model):
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    proxima_cita = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    email_usuario = models.EmailField()
    password_usuario = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


