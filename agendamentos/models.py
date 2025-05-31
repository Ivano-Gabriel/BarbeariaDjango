from django.db import models

class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=20) 
    servico = models.CharField(max_length=100, default='Corte de Cabelo')
    data_agendamento = models.DateField() 
    hora_agendamento = models.TimeField()
    status = models.CharField(max_length=50, default='pendente') 

    def __str__(self):
        return f"Agendamento de {self.nome_cliente} para {self.servico} em {self.data_agendamento} às {self.hora_agendamento}"

    class Meta:
        ordering = ['data_agendamento', 'hora_agendamento'] 
        verbose_name = "Agendamento da Barbearia"
        verbose_name_plural = "Agendamentos da Barbearia"
