from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse
from core.models import TarefaModel
from core.forms import TarefaForm
from datetime import date


def agenda(request):
    tasks = TarefaModel.objects.all()
    print(tasks)  # Optional for debugging

    return render(
        request,
        'agenda.html',
        {'tasks': tasks}
    )


def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    return HttpResponseRedirect(reverse('core:index'))


def create(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            TarefaModel.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('core:index'))
        contexto = {'form': form}
        return render(request, "cadastro.html", contexto)
    contexto = {'form': TarefaForm()}
    return render(request, 'cadastro.html', contexto)



from datetime import date

def pendentes(request):
    hoje = date.today()

    qs = TarefaModel.objects.filter(conclusao=hoje)

    if qs.exists():
        nome_tarefa = qs[0].titulo
        contexto = {'title': "Meu Compromisso", 'titulo': True, 'nome_tarefa': nome_tarefa}
    else:
        contexto = {'title': "Meu Compromisso", 'tarefas_pendentes': False}

    return render(request, 'tarefa.html', contexto)
