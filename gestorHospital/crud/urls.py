# crud/urls.py
from django.urls import path
from .views import (ServicioListView, ServicioCreateView, ServicioUpdateView, ServicioDeleteView,
                    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
                    PagoListView, PagoCreateView, PagoUpdateView, PagoDeleteView)

urlpatterns = [
    path('servicios/', ServicioListView.as_view(), name='servicio_list'),
    path('servicio/new/', ServicioCreateView.as_view(), name='servicio_create'),
    path('servicio/<int:pk>/edit/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicio/<int:pk>/delete/', ServicioDeleteView.as_view(), name='servicio_delete'),
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('paciente/new/', PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente/<int:pk>/edit/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('paciente/<int:pk>/delete/', PacienteDeleteView.as_view(), name='paciente_delete'),
    path('pagos/', PagoListView.as_view(), name='pago_list'),
    path('pago/new/', PagoCreateView.as_view(), name='pago_create'),
    path('pago/<int:pk>/edit/', PagoUpdateView.as_view(), name='pago_update'),
    path('pago/<int:pk>/delete/', PagoDeleteView.as_view(), name='pago_delete'),
]
