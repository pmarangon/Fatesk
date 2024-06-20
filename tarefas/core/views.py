from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse
from core.models import TarefaModel
from core.forms import TarefaModelForm


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
        form = TarefaModelForm(request.POST)
        if form.is_valid():
            TarefaModel.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('core:index'))
        contexto = {'form': form}
        return render(request, "cadastro.html", contexto)
    contexto = {'form': TarefaModelForm()}
    return render(request, 'cadastro.html', contexto)

