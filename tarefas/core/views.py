from django.shortcuts import render
from django.http import HttpResponse

def agenda(request):
  contexto = {'agenda': True,
              'praia': False}
  return render(request, 'index.html', contexto)
