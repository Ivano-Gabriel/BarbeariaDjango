# agendamentos/forms.py
from django import forms
from .models import Agendamento 

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento 
        fields = '__all__' 

        
        widgets = {
            'data_agendamento': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendamento': forms.TimeInput(attrs={'type': 'time'}),

        }

        labels = {
            'nome_cliente': 'Nome do Cliente',
            'telefone_cliente': 'Telefone',
            'servico': 'Serviço Desejado',
            'data_agendamento': 'Data do Agendamento',
            'hora_agendamento': 'Hora do Agendamento',
            'status': 'Status do Agendamento',
        }

        help_texts = {
            'telefone_cliente': 'Formato: (XX) XXXXX-XXXX',
        }

        error_messages = {
            'nome_cliente': {
                'max_length': "Este nome é muito longo. Por favor, abrevie.",
            },
        }