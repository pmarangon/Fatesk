from django.shortcuts import render
from django.http import HttpResponse

def agenda(request):
  return HttpResponse("Day off - sem tarefas hoje")
