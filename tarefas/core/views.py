from django.shortcuts import render
from django.http import HttpResponse
from core.models import TarefaModel


def agenda(request):
    tasks = TarefaModel.objects.all()
    print(tasks)  # Optional for debugging

    return render(
        request,
        'agenda.html',
        {'tasks': tasks}
    )

