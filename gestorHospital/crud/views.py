# crud/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Servicio, Paciente, Pago
from .forms import ServicioForm, PacienteForm, PagoForm

class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicio_list.html'

class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio_form.html'
    success_url = reverse_lazy('servicio_list')

class ServicioUpdateView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio_form.html'
    success_url = reverse_lazy('servicio_list')

class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'servicio_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')

# Similar views can be created for Paciente and Pago
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

class PagoListView(ListView):
    model = Pago
    template_name = 'pago_list.html'

class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago_form.html'
    success_url = reverse_lazy('pago_list')

class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago_form.html'
    success_url = reverse_lazy('pago_list')

class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'pago_confirm_delete.html'
    success_url = reverse_lazy('pago_list')
