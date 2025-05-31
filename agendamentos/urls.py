
from django.urls import path

from .views import lista_agendamentos_html, criar_agendamento 

urlpatterns = [
    path('', lista_agendamentos_html, name='lista-agendamentos'),

    path('novo/', criar_agendamento, name='criar-agendamento'),
]