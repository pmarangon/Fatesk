from django import forms
from django.forms  import  DateInput, SplitDateTimeWidget
from core.models import TarefaModel
from django.core.exceptions import ValidationError

class TarefaForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    inicio = forms.DateField(widget=DateInput)
    conclusao = forms.DateField(widget=SplitDateTimeWidget)
    descricao = forms.CharField(max_length=200)
    categoria = forms.CharField(max_length=200)


def clean_titulo(self):
    titulo = self.cleaned_data['titulo']
    return titulo.upper()


def clean_inicio(self):
    inicio = self.cleaned_data['inicio']
    return inicio.upper()


def clean_conclusao(self):
    conclusao = self.cleaned_data['conclusao']
    return conclusao.upper()


def clean_descricao(self):
    descricao = self.cleaned_data['descricao']  
    return descricao.upper()





    
    
    

            
        
        
    
    


