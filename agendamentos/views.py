# agendamentos/views.py

from django.shortcuts import render, redirect 
from .models import Agendamento 
from .forms import AgendamentoForm 
from datetime import datetime    

def lista_agendamentos_html(request):
    data_filtro_atual = request.GET.get('data_filtro')
    agendamentos = Agendamento.objects.all()

    if data_filtro_atual:
        try:
            data_filtrada = datetime.strptime(data_filtro_atual, '%Y-%m-%d').date()
            agendamentos = agendamentos.filter(data_agendamento=data_filtrada)
        except ValueError:
            pass

    agendamentos = agendamentos.order_by('data_agendamento', 'hora_agendamento')

    context = {
        'agendamentos': agendamentos,
        'data_filtro_atual': data_filtro_atual,
    }
    return render(request, 'agendamentos/lista_agendamentos.html', context)

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista-agendamentos-html') 
    else:
        form = AgendamentoForm() 

    return render(request, 'agendamentos/criar_agendamento.html', {'form': form})